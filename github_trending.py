import requests
from datetime import date, timedelta

REPOS_TO_SHOW = 20
API_URL = 'https://api.github.com'
REPOS_LIFETIME = 7


def get_trending_repositories(top_size):
    api_method = '/search/repositories'
    search_time_delta = date.today() - timedelta(days=REPOS_LIFETIME)
    parameters = {'q': 'created:>%s' % search_time_delta, 'sort': 'stars', 'order': 'desc', 'per_page': top_size}
    repos_list_response = requests.get(API_URL + api_method, params=parameters)
    return repos_list_response.json()['items']

if __name__ == '__main__':

    print("Top {} interesting repositories created during last week ".format(REPOS_TO_SHOW))
    repos_list = get_trending_repositories(REPOS_TO_SHOW)
    for repo in repos_list:
        print('Repository: {} \n'.format(repo['full_name']), 'Link:{} \n'.format(repo['html_url']),
              'Stars: {} \n'.format(repo['stargazers_count']),
              'Issues: {}'.format(repo['open_issues_count']))
