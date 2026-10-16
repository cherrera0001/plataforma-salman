-- ============================================================================
-- ESQUEMA PROPUESTO: Core Multi-tenant y Gobernanza Agéntica
-- ============================================================================
CREATE SCHEMA IF NOT EXISTS core;

DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_user') THEN
    CREATE ROLE app_user WITH LOGIN PASSWORD 'app_pass_local';
  END IF;
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'app_reporting') THEN
    CREATE ROLE app_reporting WITH LOGIN PASSWORD 'rep_pass_local';
  END IF;
END $$;

CREATE TABLE IF NOT EXISTS core.core_organizations (
id uuid PRIMARY KEY,
rut_tax_id varchar(20) NOT NULL UNIQUE,
legal_name varchar(255) NOT NULL,
is_active boolean DEFAULT true,
created_at timestamptz DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS core.core_tenants (
id uuid PRIMARY KEY,
organization_id uuid NOT NULL,
slug varchar(64) NOT NULL UNIQUE,
vertical_type varchar(32) NOT NULL,
is_active boolean DEFAULT true
);

CREATE TABLE IF NOT EXISTS core.core_users (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
email varchar(255) NOT NULL,
role varchar(32) NOT NULL,
is_active boolean DEFAULT true,
    CONSTRAINT uq_core_users_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE core.core_users ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.core_users FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_core_users_tenant_isolation ON core.core_users;
CREATE POLICY p_core_users_tenant_isolation ON core.core_users
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS core.core_agent_executions (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
agent_name varchar(64) NOT NULL,
action_requested varchar(128) NOT NULL,
status varchar(32) NOT NULL,
risk_level varchar(16) NOT NULL,
    CONSTRAINT uq_core_agent_executions_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE core.core_agent_executions ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.core_agent_executions FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_core_agent_executions_tenant_isolation ON core.core_agent_executions;
CREATE POLICY p_core_agent_executions_tenant_isolation ON core.core_agent_executions
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS core.core_idempotency_keys (
key_hash varchar(64) PRIMARY KEY,
tenant_id uuid NOT NULL,
resource_type varchar(64) NOT NULL,
response_status int,
locked_until timestamptz NOT NULL,
    CONSTRAINT uq_core_idempotency_keys_tenant_key UNIQUE (tenant_id, key_hash)
);

ALTER TABLE core.core_idempotency_keys ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.core_idempotency_keys FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_core_idempotency_keys_tenant_isolation ON core.core_idempotency_keys;
CREATE POLICY p_core_idempotency_keys_tenant_isolation ON core.core_idempotency_keys
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS core.core_payment_accounts (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
provider_name varchar(32) NOT NULL,
account_identifier varchar(64) NOT NULL,
is_active boolean DEFAULT true,
    CONSTRAINT uq_core_payment_accounts_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE core.core_payment_accounts ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.core_payment_accounts FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_core_payment_accounts_tenant_isolation ON core.core_payment_accounts;
CREATE POLICY p_core_payment_accounts_tenant_isolation ON core.core_payment_accounts
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS core.core_payment_transactions (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
account_id uuid NOT NULL,
amount_clp bigint NOT NULL,
status varchar(32) NOT NULL,
reconciliation_status varchar(32) NOT NULL,
    CONSTRAINT chk_amount_positive CHECK (amount_clp >= 0),
    CONSTRAINT uq_core_payment_transactions_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE core.core_payment_transactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.core_payment_transactions FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_core_payment_transactions_tenant_isolation ON core.core_payment_transactions;
CREATE POLICY p_core_payment_transactions_tenant_isolation ON core.core_payment_transactions
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
