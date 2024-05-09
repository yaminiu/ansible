# ansible
ansible playbook 
keep ansible playbook 


# ansible Function reults

```
# Convert yml to son
TASK [Convert YAML to JSON] ***************************************************
ok: [localhost]

TASK [debug] ******************************************************************
ok: [localhost] => {
    "json_data": "{\"key1\": \"value1\", \"key2\": [\"item1\", \"item2\", \"item3\"]}"
}

```

# list of dictionary 

```
    test_var:
      - name: test1
        url: googe.com
        port: "9092"
      - name: test2
        url: yahoo.com
        port: "8080"
      - name: test3
        url: value31
        port: '8081'
```

run 
```
ansible-playbook list_convert.yml

```
generate string  **"https://googe.com:9092,https://yahoo.com:8080,https://value31:8081"** which can be used in templates, useful in kafka application  configuration such as kafka mft etc.
