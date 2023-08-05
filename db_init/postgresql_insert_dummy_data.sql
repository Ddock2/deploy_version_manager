INSERT INTO customer (customer_name) 
    VALUES ('서울'), ('광주'), ('대전');

INSERT INTO version (major, minor, maintenance, patch) 
    VALUES (2, 0, 15, 8), (3, 1, 12, 2), (4, 2, 10, 0), (5, 3, 2, 1);

INSERT INTO revision (revision_value, git_commit_id)
    VALUES ('100', 'af84d16c'), ('200', '9d20a0e1'), ('300', 'c27ff016');

INSERT INTO deployment(customer_id, version_id, revision_id, deployment_date, deployment_purpose)
    VALUES (1, 1, 2, '2022-01-01', 'start'), (2, 2, 2, '2022-06-03', 'install'), (1, 3, 3, '2022-12-10', 'patch'), (3, 4, 2, '2023-04-08', 'new');

INSERT INTO os(os_name, os_version, os_kernel)
    VALUES ('Windows', '10', '22621.1992'), ('Centos', '8', 'kernel-4.18.0-326.el8.x86_64'), ('Solaris', '10', 'SunOS 5.10 Generic 147148-26'), ('Ubuntu', '22.04.0', '5.15.0-78-generic');

INSERT INTO deployment_os_map(deployment_id, os_id)
    VALUES (1, 1), (1, 3), (1, 4), (2, 1), (2, 2), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4);

INSERT INTO module(module_name)
    VALUES ('master'), ('slave'), ('client'), ('db');

INSERT INTO deployment_module_map(deployment_id, module_id)
    VALUES (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 1), (4, 2), (4, 3);
