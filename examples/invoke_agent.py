import argparse, json, requests
p=argparse.ArgumentParser()
p.add_argument("--base-url",default="http://localhost:8001")
p.add_argument("--test-case-id",default="TC001")
p.add_argument("--question",default="What is a Sev1 incident?")
a=p.parse_args()
r=requests.post(f"{a.base_url}/ask",json={"test_case_id":a.test_case_id,"question":a.question},timeout=10)
r.raise_for_status()
print(json.dumps(r.json(),indent=2))
