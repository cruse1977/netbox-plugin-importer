from core.choices import JobIntervalChoices
from netbox.jobs import JobRunner,  system_job
from django.conf import settings
import requests
import json

@system_job(interval=JobIntervalChoices.INTERVAL_HOURLY)
class CatalogPullJob(JobRunner):
    class Meta:
        name = "Custom Object Importer"

    def run(self, *args, **kwargs):
        job = requests.get("https://raw.githubusercontent.com/cruse1977/custom-object-library/refs/heads/main/catalog/catalog.json")
        with open(f"{settings.MEDIA_ROOT}/custom-objects-catalog.json", "w") as f:
            json.dump(job.json(), f)