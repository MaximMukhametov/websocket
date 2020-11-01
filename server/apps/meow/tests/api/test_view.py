from django.urls import reverse
from rest_framework.test import APIClient


def test_start_task_view():
    """Ensure start_task view return status 200."""
    url = reverse('run_task')
    response = APIClient().get(url)

    assert response.status_code == 200