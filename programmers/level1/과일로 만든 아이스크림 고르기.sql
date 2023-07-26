SELECT F.FLAVOR
FROM FIRST_HALF AS F JOIN ICECREAM_INFO AS INFO
ON F.FLAVOR = INFO.FLAVOR
WHERE F.TOTAL_ORDER > 3000 AND INFO.INGREDIENT_TYPE LIKE 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC
