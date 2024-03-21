-- A script on MySQL Triggers
DROP TRIGGER IF EXISTS order_update
DELIMITER &&
CREATE TRIGGER order_update AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantiy = quantity - NEW.number WHERE name = NEW.item_name;
END &&
DELIMITER;
