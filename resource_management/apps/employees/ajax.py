import json

from django.http import HttpResponse
from django.views import generic

from apps.employees.models import Schedule, Employee


class SubSlipAjax(generic.View):

    def post(self, request, **kwargs):

        slip_id = self.request.POST.get('slip_id', None)
        if slip_id:
            slip_id = int(slip_id)
            sub_slip = Schedule.objects.filter(id=slip_id).first()
            sub_slip.employee_sub = Employee.objects.filter(user=self.request.user).first()
            sub_slip.up_for_sub = 0
            sub_slip.save()

        return HttpResponse(json.dumps({'success': 1}), content_type="application/json")