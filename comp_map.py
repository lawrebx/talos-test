import folium
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def gen_comp_map(lat, lon, target_site, comp_list = None, dark_mode = True, network_visible = True):

    client_image = 'images/Bucees.png'

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

    folium.Marker(
        location=[33.192939,-97.094033],
        tooltip = "Murphy USA - Loop 288",
        popup = f'<div><img src=https://github.com/Talos-Data/talos-playbook/blob/59152bf0dd77a9d6afccbf9f20aba7e809299f00/images/MUSA.png alt="Murphy USA" width="100" height="100"><br /><span>High Elasticity/High Confidence</span></div>',
        icon = folium.Icon(icon = 'key', prefix = 'fa', color="red") # can add custom icon
    ).add_to(m)

    folium.Marker(
        location=[33.129523,-97.043119],
        tooltip = "RaceTrac - Swisher Rd",
        popup = f'<div><img src=https://github.com/Talos-Data/talos-playbook/blob/59152bf0dd77a9d6afccbf9f20aba7e809299f00/images/RaceTrac.png alt="RaceTrac" width="100" height="100"><br /><span>High Elasticity/High Confidence</span></div>',
        icon = folium.Icon(icon = 'droplet', prefix = 'fa', color="orange") # can add custom icon
    ).add_to(m)

    folium.Marker(
        location=[33.145703,-97.104813],
        tooltip = "Kroger - Teasley",
        popup = f'<div><img src=https://github.com/Talos-Data/talos-playbook/blob/59152bf0dd77a9d6afccbf9f20aba7e809299f00/images/Kroger.png alt="Kroger" width="100" height="100"><br /><span>High Elasticity/High Confidence</span></div>',
        icon = folium.Icon(icon = 'droplet', prefix = 'fa', color="orange") # can add custom icon
    ).add_to(m)

    if network_visible:
        key_comp_line = [(33.180382,-97.100601),(33.192939,-97.094033)]
        folium.PolyLine(key_comp_line, 
                        tooltip="Key Comp - Elasticity: 10%", 
                        color = '#ffbf00',
                        weight = 10
                        ).add_to(m)
        
        comp_line = [(33.180382,-97.100601),(33.129523,-97.043119)]
        folium.PolyLine(comp_line, 
                        tooltip="Other Comp - High Elasticity - Low Confidence", 
                        color = '#B20000',
                        weight = 1
                        ).add_to(m)

        comp_line = [(33.180382,-97.100601),(33.145703,-97.104813)]
        folium.PolyLine(comp_line, 
                        tooltip="Other Comp - Low Elasticity - High Confidence", 
                        color = '#808080',
                        weight = 7.5
                        ).add_to(m)

    return m


if __name__ == '__main__':

    comp_map = gen_comp_map(33.180382,-97.100601, 'x')

    comp_map.save('comp_map.html')