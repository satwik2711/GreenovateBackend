# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Factor, EmissionRecord, Tips, Organisation
from django.db.models import Sum
from rest_framework import status

@api_view(['GET'])
def get_emission_delta_tips(request, org_id, year1, year2):
    try:
        organisation = Organisation.objects.get(id=org_id)
    except Organisation.DoesNotExist:
        return Response({"error": "Organisation not found"}, status=404)

    factors = Factor.objects.all()
    max_delta = 0
    max_delta_factors = []

    for factor in factors:

        emission_year1 = EmissionRecord.objects.filter(
            organisation=organisation,
            sub_sub_factor__sub_factor__factor=factor,
            record_year=year1
        ).aggregate(total_emission=Sum('net_emission'))['total_emission'] or 0

        emission_year2 = EmissionRecord.objects.filter(
            organisation=organisation,
            sub_sub_factor__sub_factor__factor=factor,
            record_year=year2
        ).aggregate(total_emission=Sum('net_emission'))['total_emission'] or 0


        delta = abs(emission_year2 - emission_year1)

        if delta > max_delta:
            max_delta = delta
            max_delta_factors.append(factor)


        if len(max_delta_factors) > 2:
            max_delta_factors.remove(min(max_delta_factors, key=lambda f: abs(
                EmissionRecord.objects.filter(
                    organisation=organisation,
                    sub_sub_factor__sub_factor__factor=f,
                    record_year=year2
                ).aggregate(total_emission=Sum('net_emission'))['total_emission'] or 0 -
                EmissionRecord.objects.filter(
                    organisation=organisation,
                    sub_sub_factor__sub_factor__factor=f,
                    record_year=year1
                ).aggregate(total_emission=Sum('net_emission'))['total_emission'] or 0
            )))

    tips_for_factors = Tips.objects.filter(factor__in=max_delta_factors)
    tips_data = [{"factor": tip.factor.name, "tip": tip.tip} for tip in tips_for_factors]

    return Response({"tips": tips_data}, status=200)



@api_view(['POST'])
def add_tip(request):
    factor_id = request.data.get('factor_id')
    tip_text = request.data.get('tip')

    if not factor_id or not tip_text:
        return Response({"error": "Both factor_id and tip are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        factor = Factor.objects.get(id=factor_id)
    except Factor.DoesNotExist:
        return Response({"error": "Factor not found"}, status=status.HTTP_404_NOT_FOUND)

    tip = Tips.objects.create(factor=factor, tip=tip_text)

    return Response({"success": "Tip added successfully", "tip_id": tip.id}, status=status.HTTP_201_CREATED)
