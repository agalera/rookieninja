<html>
<head>
    <title>Rookie ninja!</title>
    <link href="/static/base.css" rel="stylesheet" type="text/css">
</head>

<body onload="CCPEVE.requestTrust('http://rookie.ninja/')">

<!-- <img src="https://image.eveonline.com/Character/{{ Eve_Charid }}_128.jpg"/>
<img src="https://image.eveonline.com/Render/{{ Eve_Shiptypeid }}_128.png"/> -->
<div class="info">
    <div class="info2"><img src="/static/imgs/Eve_Solarsystemname.png"/></div>
    <div class="info2">{{ system_info.security }} - {{ system_info.system }} - {{ system_info._id }}</div>
    <div class="info2"><img src="/static/imgs/class.png"/></div>
    <div class="info2">{{ system_info.class }}</div>
    <div class="info2"><img src="/static/imgs/moon.png"/></div>
    <div class="info2">{{ system_info.moons }}</div>
    <div class="info2"><img src="/static/imgs/planet.png"/></div>
    <div class="info2">{{ system_info.planets }}</div>
    <div class="info2"><img src="/static/imgs/star.png"/></div>
    <div class="info2">{{ system_info.belts }}</div>
    {% if system_info.effect %}
        <div class="info2"><img src="/static/imgs/effect.png"/></div>
        <div class="info2">{{ system_info.effect }}</div>
    {% endif %}
    <div class="info2"><img src="/static/imgs/region.png"/></div>
    <div class="info2">{{ system_info.region }}</div>
    <div class="info2"><img src="/static/imgs/constellation.png"/></div>
    <div class="info2">{{ system_info.constellation }}</div>
    {% if system_info.static %}
        <div class="info2"><img src="/static/imgs/static.png"/></div>
        <div class="info2">Static: </div>
            {% for sta in system_info.static %}
                <div class="info2">{{ sta }} ({{ system_info.static[sta] }})</div>
            {% endfor %}
    {% endif %}
    <div class="info2"><a href="http://evemaps.dotlan.net/system/{{ system_info.system }}" target="_blank">Dotlan</a></div>
    <div class="info2"><a href="https://zkillboard.com/system/{{ system_info._id }}/" target="_blank">zkill</a></div>
    <div class="clear_both"></div>
</div>
<div class="clear_both"></div>
{% if not trusted %}
    <div class="trusted">if you add a trusted web, automatically display the current system information</div>
{% endif %}

<!--{% if kills=='failed' %}
    <div class="zkilldown">
    Error connection to zkillboard
    </div>
{% else %}
    {% for kill in kills %}
        <div class="kill">
            <div class="ship"><img src="https://image.eveonline.com/Render/{{ kill.victim.shipTypeID }}_64.png"/></div>
            <div class="kill_right">
                <div class="date">Date: {{ kill.killTime }}</div>
                <div class="value">Value: {{ kill.zkb.totalValue }} Isk</div>
                <div class="attackers">Attackers: {{ kill.attackers|length }}</div>
            </div>
            <div class="clear_both"></div>
        </div>
    {% endfor %}
{% endif %}
    <div class="clear_both"></div>
</div>
-->
{% if fleet %}
<script src="https://code.jquery.com/jquery-1.12.3.min.js"></script>

    <script>
    fleet = "{{ fleet }}";
    server = "{{ server }}";
    system = "{{ system_info.system }}";
    trusted = "{{ trusted }}";
    cache_html = "";
    function doPoll(){
        jQuery(function($) { // On dom ready
            // Ajax call to the script above, assuming you saved it as "headers.php"
            html = "";

            $.getJSON('http://rookie.ninja/'+server+'/update/'+fleet+'/'+system, function(data) {
                    for (player_key in data.players){
                    player = data.players[player_key];
                    if (parseInt(player.last_update)+20 < parseInt(data.time)){
                         continue;
                    }
                    if (data.reload && trusted)
                    {
                        location.reload();
                    }
                    else{
                        html += '<div class="kill adapt_kill">\
                                <div class="invite"><a href="#" onclick="CCPEVE.inviteToFleet('+player_key+')"><img src="/static/imgs/add.png"/></a></div>\
                                 <div class="ship">\
                                    <img src="https://image.eveonline.com/Character/'+player_key+'_64.jpg"/><img src="https://image.eveonline.com/Render/'+player.Eve_Shiptypeid+'_64.png"/>\
                                    <div class="nameship">'+player.Eve_Shiptypename+'</div>\
                                 </div>\
                                 <div class="kill_right">\
                                     <div class="value"><div class="icon name"></div>'+player.Eve_Charname+'</div>\
                                     <div class="value"><div class="icon location"></div><a href="#" onclick="CCPEVE.setDestination('+player.Eve_Solarsystemid+');">'+player.Eve_Solarsystemname+'</a></div>\
                                     ';
                        if (player.Eve_wh != undefined)
                        {
                            html += '<div class="value"><div class="icon wh"></div>'+player.Eve_wh+'</div>\
                                     ';
                        }
                        html +=     '<div class="value"><div class="icon dscan"></div>'+player.Eve_Shipname+'</div>\
                                 </div>\
                                 <div class="clear_both"></div>\
                             </div>';

                        }
                    }
                    if (cache_html != html){
                        document.getElementById("fleet").innerHTML = html;
                        cache_html = html;
                    }
            });
        });
    }
    doPoll();
    window.setInterval(doPoll, 5000);
    </script>
    <div id="fleet"></div>
{% endif %}
</body>
</html>
