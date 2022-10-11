employee= {"name":"Tim","age":30,"birthday":"1990-03-10","job":"DevOps Engineer"}
employee["job"]="Software Engineer"
del employee["age"]
for x in employee:
    print(x,':',employee[x])
