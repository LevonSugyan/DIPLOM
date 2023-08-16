# Задание №1

SELECT c.login, COUNT(o."courierId") as order_count
FROM "Couriers" c 
LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true 
GROUP BY c.login 
ORDER BY order_count DESC;

# Задание №2

SELECT track, 
CASE 
    WHEN finished = true THEN 2 
    WHEN cancelled = true THEN -1 
    WHEN "inDelivery" = true THEN 1 
    ELSE 0 
END as status 
FROM "Orders";
