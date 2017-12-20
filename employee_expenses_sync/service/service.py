from employee_expenses_sync.repository.employee_repository import EmployeeRepository
from employee_expenses_sync.repository.organ_repository import OrganRepository


class Service:

    def save_employee(employee):
        repository = EmployeeRepository()
        repository.save(employee)

    def save_organ(organ):
        repository = OrganRepository()
        repository.save(organ)