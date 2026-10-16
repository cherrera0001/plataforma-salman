-- Setup inicial de roles y extensiones
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_user') THEN
    CREATE ROLE app_user WITH LOGIN PASSWORD 'app_pass_local';
  END IF;
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_reporting') THEN
    CREATE ROLE app_reporting WITH LOGIN PASSWORD 'rep_pass_local';
  END IF;
END $$;
