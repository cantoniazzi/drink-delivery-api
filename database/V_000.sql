CREATE TABLE IF NOT EXISTS distributor (
    id BIGSERIAL PRIMARY KEY,
    trading_name VARCHAR(150) NOT NULL,
    owner_name VARCHAR(150) NOT NULL,
    document VARCHAR(25) NOT NULL,
    coverage_area geometry(MULTIPOLYGON),
    address geometry(Point),
    created_at TIMESTAMP default current_timestamp,
    updated_at TIMESTAMP default current_timestamp,
    CONSTRAINT distributor_unique UNIQUE(document)
)