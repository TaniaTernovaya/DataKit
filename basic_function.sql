--task1
select ad_date,campaign_id,sum(spend),count(impressions),count(clicks),sum(value)
from facebook_ads_basic_daily fabd 
where ad_date is not null
group by ad_date,campaign_id



--task2
select campaign_id,(SUM(spend) / SUM(clicks)) * 100  AS CPC,
(SUM(spend) / 1000) * 100 :: float as CPM,
(CAST(SUM(clicks) as float) / SUM(impressions)) * 100  AS CPR,
(CAST((SUM(value - spend)) as float) / SUM(spend)) * 100 AS ROMI
from facebook_ads_basic_daily fabd
group by campaign_id



--task3 optional
select campaign_id, SUM(spend),(CAST((SUM(value - spend)) as float) / SUM(spend)) * 100 AS ROMI
from facebook_ads_basic_daily fabd
group by campaign_id
having SUM(spend) > 500000
order by ROMI desc 
limit 1