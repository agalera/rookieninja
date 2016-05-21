<html>
    <head>
        <title>Rookie ninja!</title>
        <link href="/static/base.css" rel="stylesheet" type="text/css">
    </head>
    <body onload="CCPEVE.requestTrust('http://rookie.ninja/')">

        <!-- <img src="https://image.eveonline.com/Character/{{ Eve_Charid }}_128.jpg"/>
        <img src="https://image.eveonline.com/Render/{{ Eve_Shiptypeid }}_128.png"/> -->
        <div class="info">
            <div class="total_players"><a href="/create_fleet">create fleet</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fleets: {{ stats.fleets }} Players: {{ stats.players }} </div>
            <div class="clear_both"></div>
        </div>
        <div class="imagenportada">
            <div class="contentimages">
                <div class="textoportada">
                    <h1>Rookie Ninja!</h1>
                </div>
                <div class="screenshot">
                    <img src="/static/imgs/screenshot.png" height="80%"/>
                </div>
                <a href="/create_fleet"><div class="create_fleet">Create fleet!</div></a>
            </div>
        </div>
    </body>
</html>
