from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scrape_script import fetch_jobs
import logging

# Configure logging
logger = logging.getLogger(__name__)

class JobListView(APIView):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        location=request.GET.get('location','')
        if not search_query:
            return Response({"error": "Search query not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            logger.info(f"Fetching jobs for search query: {search_query}")
            
            jobs = fetch_jobs(search_term=search_query,location=location)
            logger.info(f"Fetched {len(jobs)} jobs")
            return Response(jobs, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching jobs: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
