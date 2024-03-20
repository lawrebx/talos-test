import folium
import pathlib

filepath = pathlib.Path(__file__).parent.resolve()

def gen_comp_map(lat, lon, daypart = 'Morning Commute', comp_list = None, dark_mode = True, network_visible = True):

    client_image = f'{filepath}/images/Bucees.png'
    musa_image = f'{filepath}/images/MUSA.png'
    rt_image = f'{filepath}/images/RaceTrac.png'
    kgr_image = f'{filepath}/images/Kroger.png'
    chv_image = f'{filepath}/images/Chevron.png'

    client_icon = folium.CustomIcon(
            client_image,
            icon_size=(50, 50),
            icon_anchor=(25, 25),
            popup_anchor=(0, 0)
            )

    m = folium.Map(
                    location=[lat,lon],
                    tiles="Cartodb dark_matter",
                    zoom_start=13
                    )

    folium.Marker(
        location=[33.180382,-97.100601],
        tooltip = "Buc-ee's - Denton",
        popup = "Client Site",
        icon = client_icon # can add custom icon
    ).add_to(m)


    musa_daypart = {'Morning Commute': ['key','red','High Elasticity/High Confidence','Key Comp - Elasticity: 10%','#ffbf00',10],
                    'Lunch Rush': ['droplet','orange','High Elasticity/Low Confidence','Other Comp - High Elasticity - Low Confidence','#FF0000',2.5],
                    'Evening Commute': ['key','red','High Elasticity/High Confidence','Key Comp - Elasticity: 10%','#ffbf00',10],
                    'Overnight': ['droplet','orange','High Elasticity/Low Confidence','Other Comp - High Elasticity - Low Confidence','#FF0000',2.5]
                    }

    rt_daypart = {'Morning Commute': ['droplet','orange','High Elasticity/Low Confidence','Other Comp - High Elasticity - Low Confidence','#FF0000',2.5],
                    'Lunch Rush': ['key','red','High Elasticity/High Confidence','Key Comp - Elasticity: 8%','#ffbf00',10],
                    'Evening Commute': ['droplet','orange','High Elasticity/Low Confidence','Other Comp - High Elasticity - Low Confidence','#FF0000',2.5],
                    'Overnight': ['droplet','orange','Low Elasticity/High Confidence','Other Comp - Low Elasticity - High Confidence','#808080',7.5]
                    }
    
    kgr_daypart = {'Morning Commute': ['droplet','orange','Low Elasticity/High Confidence','Other Comp - Low Elasticity - High Confidence','#808080',7.5],
                    'Lunch Rush': ['droplet','orange','Low Elasticity/High Confidence','Other Comp - Low Elasticity - High Confidence','#808080',7.5],
                    'Evening Commute': ['droplet','orange','Low Elasticity/High Confidence','Other Comp - Low Elasticity - High Confidence','#808080',7.5],
                    'Overnight': ['droplet','orange','Low Elasticity/High Confidence','Other Comp - Low Elasticity - High Confidence','#808080',7.5]
                    }
    
    chv_daypart = {'Morning Commute': ['droplet','orange','Low Elasticity/Low Confidence','Other Comp - Low Elasticity - Low Confidence','#808080',2.5],
                    'Lunch Rush': ['droplet','orange','Low Elasticity/Low Confidence','Other Comp - Low Elasticity - Low Confidence','#808080',2.5],
                    'Evening Commute': ['droplet','orange','Low Elasticity/Low Confidence','Other Comp - Low Elasticity - Low Confidence','#808080',2.5],
                    'Overnight': ['key','red','High Elasticity/High Confidence','Key Comp - Elasticity: 5%','#ffbf00',10]
                    }

    folium.Marker(
        location=[33.192939,-97.094033],
        tooltip = "Murphy USA - Loop 288",
        popup = f"""<div>
                    <img src="{musa_image}" alt="Murphy USA" width="100" height="100">
                    <br /><span>{musa_daypart[daypart][2]}</span>
                    </div>""",
        icon = folium.Icon(icon = musa_daypart[daypart][0], prefix = 'fa', color=musa_daypart[daypart][1]) # can add custom icon
    ).add_to(m)

    folium.Marker(
        location=[33.129523,-97.043119],
        tooltip = "RaceTrac - Swisher Rd",
        popup = f"""<div>
                    <img src="{musa_image}" alt="RaceTrac" width="100" height="100">
                    <br /><span>{rt_daypart[daypart][2]}</span>
                    </div>""",
        icon = folium.Icon(icon = rt_daypart[daypart][0], prefix = 'fa', color=rt_daypart[daypart][1]) # can add custom icon
    ).add_to(m)

    folium.Marker(
        location=[33.145703,-97.104813],
        tooltip = "Kroger - Teasley",
        popup = f"""<div>
                    <img src="{musa_image}" alt="Kroger" width="100" height="100">
                    <br /><span>{kgr_daypart[daypart][2]}</span>
                    </div>""",
        icon = folium.Icon(icon = kgr_daypart[daypart][0], prefix = 'fa', color=kgr_daypart[daypart][1]) # can add custom icon
    ).add_to(m)

    folium.Marker(
        location=[33.185532,-97.108044],
        tooltip = "Chevron",
        popup = f"""<div>
                    <img src="{musa_image}" alt="Chevron" width="100" height="100">
                    <br /><span>{chv_daypart[daypart][2]}</span>
                    </div>""",
        icon = folium.Icon(icon = chv_daypart[daypart][0], prefix = 'fa', color=chv_daypart[daypart][1]) # can add custom icon
    ).add_to(m)

    if network_visible:
        key_comp_line = [(33.180382,-97.100601),(33.192939,-97.094033)]
        folium.PolyLine(key_comp_line, 
                        tooltip = musa_daypart[daypart][3], 
                        color = musa_daypart[daypart][4],
                        weight = musa_daypart[daypart][5]
                        ).add_to(m)
        
        comp_line = [(33.180382,-97.100601),(33.129523,-97.043119)]
        folium.PolyLine(comp_line, 
                        tooltip = rt_daypart[daypart][3], 
                        color = rt_daypart[daypart][4],
                        weight = rt_daypart[daypart][5]
                        ).add_to(m)

        comp_line = [(33.180382,-97.100601),(33.145703,-97.104813)]
        folium.PolyLine(comp_line, 
                        tooltip = kgr_daypart[daypart][3], 
                        color = kgr_daypart[daypart][4],
                        weight = kgr_daypart[daypart][5]
                        ).add_to(m)
        comp_line = [(33.180382,-97.100601),(33.185532,-97.108044)]
        folium.PolyLine(comp_line, 
                        tooltip = chv_daypart[daypart][3], 
                        color = chv_daypart[daypart][4],
                        weight = chv_daypart[daypart][5]
                        ).add_to(m)
    return m


if __name__ == '__main__':

    comp_map = gen_comp_map(33.180382,-97.100601)

    comp_map.save('comp_map.html')