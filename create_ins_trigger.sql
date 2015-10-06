#Run initSqlTables 1st

#This function parses data to correct partition
CREATE OR REPLACE FUNCTION set_top.vuer_data_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF ( NEW.logdate >= DATE '2014-01-01' AND NEW.logdate < DATE '2014-02-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m01 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-02-01' AND NEW.logdate < DATE '2014-03-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m02 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-03-01' AND NEW.logdate < DATE '2014-04-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m03 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-04-01' AND NEW.logdate < DATE '2014-05-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m04 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-05-01' AND NEW.logdate < DATE '2014-06-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m05 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-06-01' AND NEW.logdate < DATE '2014-07-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m06 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-07-01' AND NEW.logdate < DATE '2014-08-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m07 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-08-01' AND NEW.logdate < DATE '2014-09-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m08 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-09-01' AND NEW.logdate < DATE '2014-10-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m09 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-10-01' AND NEW.logdate < DATE '2014-11-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m10 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-11-01' AND NEW.logdate < DATE '2014-12-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m11 VALUES (NEW.*);
    ELSIF ( NEW.logdate >= DATE '2014-12-01' AND NEW.logdate < DATE '2015-01-01' ) THEN
        INSERT INTO set_top.vuer_data_y2014m12 VALUES (NEW.*);

    ELSE
        RAISE EXCEPTION 'Date out of range.  Fix the vuer_data_insert_trigger() function!';
    END IF;
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER insert_vuer_data_trigger
    BEFORE INSERT ON set_top.vuetrakmstr
    FOR EACH ROW EXECUTE PROCEDURE set_top.vuer_data_insert_trigger();