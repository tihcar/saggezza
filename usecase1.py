import snowflake.connector
import base64
import requests
import sys

def main(argv):
    ACCOUNT = 'ib52967'
    USER = 'yourusername'
    PASSWORD = 'yourpassword'
    
    con = snowflake.connector.connect(
      user=USER,
      password=PASSWORD,
      account=ACCOUNT,
    )
    
    # =============================================================================
    # con.cursor().execute("use warehouse saggezza_wh_2;")
    # con.cursor().execute("use database demo_db")
    # con.cursor().execute("use schema public")
    # =============================================================================
    
# =============================================================================
#     user = 'tihcar'
#     repo_name = 'saggezza'
#     path_to_file = 'RRD/usecase1.sql'
# =============================================================================
    user = argv[0]
    repo_name = argv[1]
    path_to_file = argv[2]
    
    print('Fetching script from')
    print('https://raw.githubusercontent.com/{0}/{1}/master/{2}'.format(user,repo_name,path_to_file))
    
    # =============================================================================
    # url = 'https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}'
    # url = 'https://api.github.com/repos/tihcar/saggezza/contents/RRD/usecase1.sql'
    # 
    # req = requests.get(url)
    # con = req.json()['content']
    # content = base64.decode(con)
    # =============================================================================
    page = requests.get('https://raw.githubusercontent.com/{0}/{1}/master/{2}'.format(user,repo_name,path_to_file))
    
    if page.status_code == 200:
        print('script fetched successfully, executing script now')
        queries = page.text.split(';')
        
        for query in queries:
            if len(query) > 0:
                ##print('Executing' + query)
                con.cursor().execute(query)
    else:
        print('script fetched failed, Aborting')

if __name__ == '__main__':
    main(sys.argv[1:])
