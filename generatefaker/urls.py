from django.conf.urls import url
from generatefaker.generate_fake_data import faker

urlpatterns = [
    url(r'^generate_faker', faker.as_view() ,name="generate-faker"),
]