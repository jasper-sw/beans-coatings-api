CREATE TABLE IF NOT EXISTS jobs (
    uuid text,
    job_type text,
    job_name text,
    job_status text,
    progress text,
    date_created integer,
    date_completed integer,
    due_date integer,
    customer_uuid text
);