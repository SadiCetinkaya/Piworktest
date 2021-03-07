SELECT CC.country, CC.date,  
CASE
WHEN daily_vaccinations is NULL THEN 0 else daily_vaccinations 
END  as daily_vaccinations,
CC.vaccines
FROM
(SELECT AA.country, AA.date,  
CASE
WHEN daily_vaccinations is NULL THEN (select median(daily_vaccinations) from table_vacc BB where BB.country = AA.country) else daily_vaccinations 
END  as daily_vaccinations,
vaccines
FROM table_vacc AA) CC;