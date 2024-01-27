#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True)
        )
    )

    file_path = module.params['path']
    file_exists = os.path.exists(file_path)

    module.exit_json(changed=False, path=file_path, exists=file_exists)

if __name__ == '__main__':
    main()