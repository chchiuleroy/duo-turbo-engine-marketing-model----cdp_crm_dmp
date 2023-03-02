import dash, numpy as np
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.P([
        dcc.Dropdown(
        id = 'my_dropdown',
        options = [
            {'label': '會員人數之增長情況', 'value': 0},
            {'label': '會員曾購買之人數增長情況', 'value': 1},
            {'label': '訪次(visitors)之增長情況', 'value': 2},
            {'label': '轉換率(conversion rate)之增長情況', 'value': 3}
            ],
        value = 0
        )
        ], style = {
        'width': '20%',
        'fontSize' : '16px',
        'display': 'inline-block'
                }
            ),
        
    dcc.Graph(id = 'my_graph'),
    
    html.P([
    html.Label('過去一年累積會員人數'),
    dcc.Slider(
        id = 'customer',
        min = 5000,
        max = 35000,
        value = 10000,
        marks = {i: str(i) for i in range(5000, 40000, 5000)}
     ),
    html.Label('過去一年曾經購買的會員人數(不重複)'),
    dcc.Slider(
        id = 'customer_buy',
        min = 100,
        max = 700,
        value = 250,
        marks = {i: str(i) for i in range(100, 750, 50)}
    ),
    html.Label('過去一年累積訪次(visitors)'),
    dcc.Slider(
        id = 'visitors',
        min = 100000,
        max = 1000000,
        value = 200000,
        marks = {i: str(i) for i in range(100000, 1100000, 100000)}
    ),
    html.Label('過去一年轉換率(conversion rate)'),
    dcc.Slider(
        id = 'conversion',
        min = 1,
        max = 10,
        value = 2,
        marks = {i: str(i/10000) for i in range(1, 11, 1)}
    ),
    html.Label('今年投入內容優化預算'),
    dcc.Slider(
        id = 'content_budget',
        min = 1000000,
        max = 5000000,
        value = 1000000,
        step = 500000,
        marks = {i: str(i) for i in range(1000000, 5500000, 500000)}
    ),
    html.Label('今年投入廣告預算'),
    dcc.Slider(
        id = 'ad_budget',
        min = 1000000,
        max = 5000000,
        value = 3000000,
        step = 500000,
        marks = {i: str(i) for i in range(1000000, 5500000, 500000)}
    ),
    html.Label('可能的CPC'),
    dcc.Slider(
        id = 'cpc_max',
        min = 1,
        max = 10,
        value = 5,
        marks = {i: str(i) for i in range(1, 11)}
    ),
    html.Label('執行週數'),
    dcc.Slider(
        id = 'duration(week)',
        min = 1,
        max = 52,
        value = 52,
        marks = {i: str(i) for i in range(1, 53, 3)}
    ),
    html.Label('每週自然增加訪次區間'),
    dcc.RangeSlider(
        id = 'weekly_vititors_range',
        min = 3000,
        max = 10000,
        value = [3000, 6000],
        marks = {i: str(i) for i in range(3000, 10500, 500)}
    ),
    html.Label('每週自然進入網站比例上限區間'),
    dcc.RangeSlider(
        id = 'entery_pecentage_range',
        min = 70,
        max = 95,
        value = [70, 90],
        marks = {i: str(i/100) for i in range(70, 100, 5)}
    ),
    html.Label('每週自然進入網站並成為會員比例區間'),
    dcc.RangeSlider(
        id = 'become_customer_pecetage_range',
        min = 10,
        max = 50,
        value = [10, 30],
        marks = {i: str(i/100) for i in range(10, 55, 5)}
    ),
    html.Label('每週自然成為會員並購買比例區間'),
    dcc.RangeSlider(
        id = 'buy_pecentage_range',
        min = 10,
        max = 100,
        value = [10, 20],
        marks = {i: str(i/10000) for i in range(10, 100, 10)}
    ),
    html.Label('因廣告進入網站比例上限區間'),
    dcc.RangeSlider(
        id = 'entery_ad_pecentage_range',
        min = 20,
        max = 60,
        value = [30, 40],
        marks = {i: str(i/100) for i in range(20, 65, 5)}
    ),
    html.Label('因廣告成為會員比例區間'),
    dcc.RangeSlider(
        id = 'become_customer_ad_pecetage_range',
        min = 10,
        max = 40,
        value = [10, 25],
        marks = {i: str(i/100) for i in range(10, 43, 3)}
    ),
    html.Label('因廣告成為會員並購買比例區間'),
    dcc.RangeSlider(
        id = 'buy_ad_pecentage_range',
        min = 10,
        max = 40,
        value = [10, 25],
        marks = {i: str(i/1000) for i in range(10, 45, 5)}
    ),
    html.Label('因內容優化進入網站比例上限區間'),
    dcc.RangeSlider(
        id = 'entery_content_pecentage_range',
        min = 50,
        max = 90,
        value = [60, 80],
        marks = {i: str(i/100) for i in range(50, 95, 5)}
    ),
    html.Label('因內容成為會員比例區間'),
    dcc.RangeSlider(
        id = 'become_customer_content_pecetage_range',
        min = 10,
        max = 40,
        value = [15, 30],
        marks = {i: str(i/100) for i in range(10, 45, 5)}
    ),
    html.Label('因內容成為會員並購買比例區間'),
    dcc.RangeSlider(
        id = 'buy_content_pecentage_range',
        min = 10,
        max = 100,
        value = [20, 50],
        marks = {i: str(i/1000) for i in range(10, 110, 10)}
    ),
    html.Label('每週因會員推薦增加訪次區間'),
    dcc.RangeSlider(
        id = 'weekly_recommnd_vititors_range',
        min = 500,
        max = 3000,
        value = [500, 1500],
        marks = {i: str(i) for i in range(500, 3250, 250)}
    ),
    html.Label('因會員推薦進入網站比例上限區間'),
    dcc.RangeSlider(
        id = 'entery_recommnd_pecentage_range',
        min = 60,
        max = 90,
        value = [60, 80],
        marks = {i: str(i/100) for i in range(60, 95, 5)}
    ),
    html.Label('因會員推薦成為會員比例區間'),
    dcc.RangeSlider(
        id = 'become_customer_recommnd_pecetage_range',
        min = 50,
        max = 90,
        value = [70, 90],
        marks = {i: str(i/100) for i in range(50, 95, 5)}
    ),
    html.Label('因會員推薦而購買比例區間'),
    dcc.RangeSlider(
        id = 'buy_recommnd_pecentage_range',
        min = 40,
        max = 90,
        value = [50, 80],
        marks = {i: str(i/1000) for i in range(40, 95, 5)}
    )
    ], style = {
        'width': '100%',
        'fontSize' : '14px',
                }),
]
            )

@app.callback(Output('my_graph', 'figure'), [Input('my_dropdown', 'value'), Input('customer', 'value'), 
                                             Input('customer_buy', 'value'), Input('visitors', 'value'), 
                                             Input('conversion', 'value'), Input('content_budget', 'value'), 
                                             Input('ad_budget', 'value'), Input('cpc_max', 'value'),
                                             Input('duration(week)', 'value'),
                                             
                                             Input('weekly_vititors_range', 'value'),
                                             Input('entery_pecentage_range', 'value'),
                                             Input('become_customer_pecetage_range', 'value'),
                                             Input('buy_pecentage_range', 'value'),
                                             
                                             Input('entery_ad_pecentage_range', 'value'),
                                             Input('become_customer_ad_pecetage_range', 'value'),
                                             Input('buy_ad_pecentage_range', 'value'),
                                             
                                             Input('entery_content_pecentage_range', 'value'),
                                             Input('become_customer_content_pecetage_range', 'value'),
                                             Input('buy_content_pecentage_range', 'value'),
                                             
                                             Input('weekly_recommnd_vititors_range', 'value'),
                                             Input('entery_recommnd_pecentage_range', 'value'),
                                             Input('become_customer_recommnd_pecetage_range', 'value'),
                                             Input('buy_recommnd_pecentage_range', 'value')
                                             ])
def update_graph(dropdown, customer, customer_buy, visitors, conversion, content_budget, ad_budget, cpc_max, duration,
                 weekly_vititors_range, entery_pecentage_range, become_customer_pecetage_range, buy_pecentage_range, 
                 entery_ad_pecentage_range, become_customer_ad_pecetage_range, buy_ad_pecentage_range,
                 entery_content_pecentage_range, become_customer_content_pecetage_range, buy_content_pecentage_range,
                 weekly_recommnd_vititors_range, entery_recommnd_pecentage_range, become_customer_recommnd_pecetage_range,
                 buy_recommnd_pecentage_range
                 ):
    
    def duration_nature_change(duration, weekly_vititors_range, entery_pecentage_range, become_customer_pecetage_range, buy_pecentage_range):
        duration_visitors = np.random.randint(weekly_vititors_range[0], weekly_vititors_range[1], duration)
        duration_sessions = np.round(duration_visitors*np.random.uniform(1.1, 1.5, duration))
        duration_entery = np.round(np.random.uniform(entery_pecentage_range[0]/100, entery_pecentage_range[1]/100, duration)*duration_visitors)
        duration_become_customer = np.round(np.random.uniform(become_customer_pecetage_range[0]/100, become_customer_pecetage_range[1]/100, duration)*duration_entery)
        duration_buy = np.round(np.random.uniform(buy_pecentage_range[0]/10000, buy_pecentage_range[1]/10000, duration)*duration_become_customer)
        duration_buy_volume = np.round(duration_buy*np.random.uniform(1.1, 1.5, duration))
        return duration_visitors, duration_sessions, duration_entery, duration_become_customer, duration_buy, duration_buy_volume
    
    def duration_content_effect(duration, content_budget, entery_content_pecentage_range, become_customer_content_pecetage_range, buy_content_pecentage_range):
        if duration < 26:
            visitors_content = np.array([int(content_budget**(0.5)*3)]*duration)
        elif duration >= 26:
            visitors_content = np.array([int(content_budget**(0.5)*3)]*25 + [int(content_budget**(0.625)*5)]*(duration - 25))
        session_content = np.round(visitors_content*np.random.uniform(1.2, 1.8, duration))
        entry_content = np.round(visitors_content*np.random.uniform(entery_content_pecentage_range[0]/100, entery_content_pecentage_range[1]/100, duration))
        become_customer_content = np.round(entry_content*np.random.uniform(become_customer_content_pecetage_range[0]/100, become_customer_content_pecetage_range[1]/100, duration))
        buy_content = np.round(become_customer_content*np.random.uniform(buy_content_pecentage_range[0]/1000, buy_content_pecentage_range[1]/1000, duration))
        buy_volume_content = np.round(buy_content*np.random.uniform(1.1, 1.2, duration))
        return visitors_content, session_content, entry_content, become_customer_content, buy_content, buy_volume_content
    
    def duration_content_effect_notwell(duration, content_budget, entery_content_pecentage_range, become_customer_content_pecetage_range, buy_content_pecentage_range):
        visitors_content = np.array([int(content_budget**(0.5)*1.2)]*duration)
        session_content = np.round(visitors_content*np.random.uniform(1.5, 2.0, duration))
        entry_content = np.round(visitors_content*np.random.uniform(entery_content_pecentage_range[0]/100, entery_content_pecentage_range[1]/100, duration))
        become_customer_content = np.round(entry_content*np.random.uniform(become_customer_content_pecetage_range[0]/100, become_customer_content_pecetage_range[1]/100, duration))
        buy_content = np.round(become_customer_content*np.random.uniform(buy_content_pecentage_range[0]/1000, buy_content_pecentage_range[1]/1000, duration))
        buy_volume_content = np.round(buy_content*np.random.uniform(1.05, 1.1, duration))
        return visitors_content, session_content, entry_content, become_customer_content, buy_content, buy_volume_content
        
    def duration_ad_effect(duration, ad_budget, cpc_max, entery_ad_pecentage_range, become_customer_ad_pecetage_range, buy_ad_pecentage_range):
        visitors_ad = np.round([int((ad_budget/cpc_max*0.6/52)*0.5)]*duration)
        session_ad = np.round(visitors_ad*np.random.uniform(1.5, 2.0, duration))
        entry_ad = np.round(visitors_ad*np.random.uniform(entery_ad_pecentage_range[0]/100, entery_ad_pecentage_range[1]/100, duration))
        become_customer_ad = np.round(entry_ad*np.random.uniform(become_customer_ad_pecetage_range[0]/100, become_customer_ad_pecetage_range[1]/100, duration))
        buy_ad = np.round(become_customer_ad*np.random.uniform(buy_ad_pecentage_range[0]/1000, buy_ad_pecentage_range[1]/1000, duration))
        buy_volume_ad = np.round(buy_ad*np.random.uniform(1.1, 1.3, duration))
        return visitors_ad, session_ad, entry_ad, become_customer_ad, buy_ad, buy_volume_ad
    
    def duration_ad_effect_notwell(duration, ad_budget, cpc_max, entery_ad_pecentage_range, become_customer_ad_pecetage_range, buy_ad_pecentage_range):
        visitors_ad = np.round([int((ad_budget/cpc_max*0.6/52)*0.3)]*duration)
        session_ad = np.round(visitors_ad*np.random.uniform(1.1, 1.5, duration))
        entry_ad = np.round(visitors_ad*np.random.uniform(entery_ad_pecentage_range[0]/100, entery_ad_pecentage_range[1]/100, duration))
        become_customer_ad = np.round(entry_ad*np.random.uniform(become_customer_ad_pecetage_range[0]/100, become_customer_ad_pecetage_range[1]/100, duration))
        buy_ad = np.round(become_customer_ad*np.random.uniform(buy_ad_pecentage_range[0]/1000, buy_ad_pecentage_range[1]/1000, duration))
        buy_volume_ad = np.round(buy_ad*np.random.uniform(1.3, 1.5, duration))
        return visitors_ad, session_ad, entry_ad, become_customer_ad, buy_ad, buy_volume_ad
    
    def duration_recommand_effect(duration, weekly_recommnd_vititors_range, entery_recommnd_pecentage_range, become_customer_recommnd_pecetage_range, buy_recommnd_pecentage_range):
        if duration < 26:
            visitors_recommand = np.random.randint(weekly_recommnd_vititors_range[0], weekly_recommnd_vititors_range[1], duration)
        elif duration >= 26:
            visitors_recommand = np.round(np.random.randint(weekly_recommnd_vititors_range[0], weekly_recommnd_vititors_range[1], duration)**1.2)
        session_recommand = np.round(visitors_recommand*np.random.uniform(1.2, 1.6, duration))
        entry_recommand = np.round(visitors_recommand*np.random.uniform(entery_recommnd_pecentage_range[0]/100, entery_recommnd_pecentage_range[1]/100, duration))
        become_customer_recommand = np.round(entry_recommand*np.random.uniform(become_customer_recommnd_pecetage_range[0]/100, become_customer_recommnd_pecetage_range[1]/100, duration))
        buy_recommand = np.round(become_customer_recommand*np.random.uniform(buy_recommnd_pecentage_range[0]/1000, buy_recommnd_pecentage_range[1]/1000, duration))
        buy_volume_recommand = np.round(buy_recommand*np.random.uniform(1.3, 1.8, duration))
        return visitors_recommand, session_recommand, entry_recommand, become_customer_recommand, buy_recommand, buy_volume_recommand
    
    def duration_recommand_effect_notwell(duration, weekly_recommnd_vititors_range, entery_recommnd_pecentage_range, become_customer_recommnd_pecetage_range, buy_recommnd_pecentage_range):
        visitors_recommand = np.round(np.random.randint(weekly_recommnd_vititors_range[0], weekly_recommnd_vititors_range[1], duration)*0.5)
        session_recommand = np.round(visitors_recommand*np.random.uniform(1.8, 2.2, duration))
        entry_recommand = np.round(visitors_recommand*np.random.uniform(entery_recommnd_pecentage_range[0]/100, entery_recommnd_pecentage_range[1]/100, duration))
        become_customer_recommand = np.round(entry_recommand*np.random.uniform(become_customer_recommnd_pecetage_range[0]/100, become_customer_recommnd_pecetage_range[1]/100, duration))
        buy_recommand = np.round(become_customer_recommand*np.random.uniform(buy_recommnd_pecentage_range[0]/1000, buy_recommnd_pecentage_range[1]/1000, duration))
        buy_volume_recommand = np.round(buy_recommand*np.random.uniform(1.1, 1.2, duration))
        return visitors_recommand, session_recommand, entry_recommand, become_customer_recommand, buy_recommand, buy_volume_recommand
    
    nature = duration_nature_change(duration, weekly_vititors_range, entery_pecentage_range, become_customer_pecetage_range, buy_pecentage_range)
    content = duration_content_effect(duration, content_budget, entery_content_pecentage_range, become_customer_content_pecetage_range, buy_content_pecentage_range)
    ad = duration_ad_effect(duration, ad_budget, cpc_max, entery_ad_pecentage_range, become_customer_ad_pecetage_range, buy_ad_pecentage_range)
    recommand = duration_recommand_effect(duration, weekly_recommnd_vititors_range, entery_recommnd_pecentage_range, become_customer_recommnd_pecetage_range, buy_recommnd_pecentage_range)
    
    content_notwell = duration_content_effect_notwell(duration, content_budget, entery_content_pecentage_range, become_customer_content_pecetage_range, buy_content_pecentage_range)
    ad_notwell = duration_ad_effect_notwell(duration, ad_budget, cpc_max, entery_ad_pecentage_range, become_customer_ad_pecetage_range, buy_ad_pecentage_range)
    recommand_notwell = duration_recommand_effect_notwell(duration, weekly_recommnd_vititors_range, entery_recommnd_pecentage_range, become_customer_recommnd_pecetage_range, buy_recommnd_pecentage_range)
    
    session = visitors*np.random.uniform(1.1, 1.3)
    buy_volume = session*conversion/10000
    
    all_visitors = np.cumsum(np.array([visitors] + (nature[0] + content[0] + ad[0] + recommand[0]).tolist()))
    all_session = np.cumsum(np.array([session] + (nature[1] + content[1] + ad[1] + recommand[1]).tolist()))
    all_customer = np.cumsum(np.array([customer] + (nature[3] + content[3] + ad[3] + recommand[3]).tolist()))
    all_customer_buy = np.cumsum(np.array([customer_buy] + (nature[4] + content[4] + ad[4] + recommand[4]).tolist()))
    all_buy_volume = np.cumsum(np.array([buy_volume] + (nature[5] + content[5] + ad[5] + recommand[5]).tolist()))
    all_conversion = np.sort(all_buy_volume/all_session)

    all_poor_visitors = np.cumsum(np.array([visitors] + (nature[0] + content_notwell[0] + ad_notwell[0] + recommand_notwell[0]).tolist()))
    all_poor_session = np.cumsum(np.array([session] + (nature[1] + content_notwell[1] + ad_notwell[1] + recommand_notwell[1]).tolist()))
    all_poor_customer = np.cumsum(np.array([customer] + (nature[3] + content_notwell[3] + ad_notwell[3] + recommand_notwell[3]).tolist()))
    all_poor_customer_buy = np.cumsum(np.array([customer_buy] + (nature[4] + content_notwell[4] + ad_notwell[4] + recommand_notwell[4]).tolist()))
    all_poor_buy_volume = np.cumsum(np.array([buy_volume] + (nature[5] + content_notwell[5] + ad_notwell[5] + recommand_notwell[5]).tolist()))
    all_poor_conversion = np.sort(all_poor_buy_volume/all_poor_session)    
    
    dmp_visitors = np.cumsum(np.array([visitors] + (nature[0] + ad_notwell[0]).tolist()))
    dmp_session = np.cumsum(np.array([session] + (nature[1] + ad_notwell[1]).tolist()))
    dmp_customer = np.cumsum(np.array([customer] + (nature[3] + ad_notwell[3]).tolist()))
    dmp_customer_buy = np.cumsum(np.array([customer_buy] + (nature[4] + ad_notwell[4]).tolist()))
    dmp_buy_volume = np.cumsum(np.array([buy_volume] + (nature[5] + ad_notwell[5]).tolist()))
    dmp_conversion = np.sort(dmp_buy_volume/dmp_session)
    
    crm_poor_visitors = np.cumsum(np.array([visitors] + (nature[0] + content_notwell[0]).tolist()))
    crm_poor_session = np.cumsum(np.array([session] + (nature[1] + content_notwell[1]).tolist()))
    crm_poor_customer = np.cumsum(np.array([customer] + (nature[3] + content_notwell[3]).tolist()))
    crm_poor_customer_buy = np.cumsum(np.array([customer_buy] + (nature[4] + content_notwell[4]).tolist()))
    crm_poor_buy_volume = np.cumsum(np.array([buy_volume] + (nature[5] + content_notwell[5]).tolist()))
    crm_poor_conversion = np.sort(crm_poor_buy_volume/crm_poor_session)
    
    dataset = [[crm_poor_customer, dmp_customer, all_poor_customer, all_customer], 
               [crm_poor_customer_buy, dmp_customer_buy, all_poor_customer_buy, all_customer_buy], 
               [crm_poor_visitors, dmp_visitors, all_poor_visitors, all_visitors],
               [crm_poor_conversion, dmp_conversion, all_poor_conversion, all_conversion]]
    
    df = dataset[dropdown]
    
    return {
        'data': [
                {'x': list(range(duration+1)), 'y': df[0], 'type':'line', 'name': '只使用CRM的情況'},
                {'x': list(range(duration+1)), 'y': df[1], 'type':'line', 'name': '只使用DMP的情況'},
                {'x': list(range(duration+1)), 'y': df[2], 'type':'line', 'name': '使用行銷雙渦輪 -- 一般情況'},
                {'x': list(range(duration+1)), 'y': df[3], 'type':'line', 'name': '使用行銷雙渦輪 -- 手法優化'}
                ],
        'layout': {
            'xaxis': {
                'title': 'week', 
                'showgrid': False
            },
            'yaxis': {
                'showgrid': False
            }}
    }


if __name__ == '__main__':
    app.run_server()