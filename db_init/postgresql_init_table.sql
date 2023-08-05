DROP TABLE deployment_os_map;
DROP TABLE os;
DROP TABLE deployment_module_map;
DROP TABLE module;
DROP TABLE deployment;
DROP TABLE customer;
DROP TABLE version;
DROP TABLE revision;


CREATE TABLE customer (
    customer_id     SERIAL PRIMARY KEY,
    customer_name   TEXT UNIQUE
);

CREATE TABLE version (
    version_id      SERIAL PRIMARY KEY,
    major           int NOT NULL,
    minor           int NOT NULL,
    maintenance     int NOT NULL,
    patch           int NOT NULL,
    UNIQUE(major, minor, maintenance, patch)
);

CREATE TABLE revision (
    revision_id     SERIAL PRIMARY KEY,
    revision_value  TEXT UNIQUE,
    git_commit_id   TEXT NOT NULL
);

CREATE TABLE deployment (
    deployment_id       SERIAL PRIMARY KEY,
    customer_id         INT NOT NULL,
    version_id          INT NOT NULL,
    revision_id         INT NOT NULL,
    deployment_date     DATE NOT NULL,
    deployment_purpose  TEXT,
    FOREIGN KEY (customer_id)   REFERENCES customer(customer_id),
    FOREIGN KEY (version_id)    REFERENCES version(version_id),
    FOREIGN KEY (revision_id)   REFERENCES revision(revision_id)
);


CREATE TABLE os (
    os_id           SERIAL PRIMARY KEY,
    os_name         TEXT UNIQUE,
    os_version      TEXT NOT NULL,
    os_kernel       TEXT NOT NULL
);

CREATE TABLE deployment_os_map (
    deployment_os_map_id    SERIAL PRIMARY KEY,
    deployment_id           INT NOT NULL,
    os_id                   INT NOT NULL,
    FOREIGN KEY (deployment_id)    REFERENCES deployment(deployment_id),
    FOREIGN KEY (os_id)   REFERENCES os(os_id),
    UNIQUE(deployment_id, os_id)
);


CREATE TABLE module (
    module_id       SERIAL PRIMARY KEY,
    module_name     TEXT UNIQUE
);

CREATE TABLE deployment_module_map (
    deployment_module_map_id    SERIAL PRIMARY KEY,
    deployment_id               INT NOT NULL,
    module_id                   INT NOT NULL,
    FOREIGN KEY (deployment_id)    REFERENCES deployment(deployment_id),
    FOREIGN KEY (module_id)   REFERENCES module(module_id),
    UNIQUE(deployment_id, module_id)
);
