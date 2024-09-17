import pandas as pd
from mplsoccer import Radar, FontManager, grid,PyPizza
import streamlit as st

font_normal = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Regular.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/'
                          'src/hinted/Roboto-Italic.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab[wght].ttf')

df=pd.read_csv('new_data.csv')

pos_col={
    'GK':['now_cost', 'points_per_game', 'selected_by_percent',
       'total_points', 'value_season', 'minutes', 'clean_sheets',
       'clean_sheets_per_90', 'goals_conceded','penalties_saved',
       'saves_per_90', 'yellow_cards','saves','bonus', 'bps',
       'starts','expected_goals_conceded', 'expected_goals_conceded_per_90',
       'goals_conceded_per_90'],
    'DEF':['now_cost', 'points_per_game', 'selected_by_percent',
       'total_points', 'value_season', 'minutes', 'goals_scored',
       'assists', 'clean_sheets', 'goals_conceded', 'own_goals','yellow_cards', 'red_cards', 'bonus', 'bps',
       'influence', 'creativity', 'threat', 'ict_index', 'starts',
       'expected_goals', 'expected_assists', 'expected_goal_involvements',
       'expected_goals_per_90', 'expected_assists_per_90',
       'expected_goal_involvements_per_90'],
       'MID':['now_cost', 'points_per_game', 'selected_by_percent',
       'total_points', 'value_season', 'minutes',
       'goals_scored', 'assists','penalties_missed', 'yellow_cards',
       'red_cards', 'bonus', 'bps', 'influence', 'creativity',
       'threat', 'ict_index', 'starts', 'expected_goals', 'expected_assists',
       'expected_goal_involvements', 'expected_goals_per_90',
       'expected_assists_per_90', 'expected_goal_involvements_per_90'],
       'FWD':['now_cost', 'points_per_game', 'selected_by_percent',
       'total_points', 'value_season', 'minutes',
       'goals_scored', 'assists','penalties_missed', 'yellow_cards',
       'red_cards', 'bonus', 'bps', 'influence', 'creativity',
       'threat', 'ict_index', 'starts', 'expected_goals', 'expected_assists',
       'expected_goal_involvements', 'expected_goals_per_90',
       'expected_assists_per_90', 'expected_goal_involvements_per_90']
           
}
pos_name={

    'GK': ['now_cost', 'ppgame', 'selected_percent',
       'T_pts', 'value_season', 'minutes', 'C_Sheets',
       'CS_90', 'GC','P_saved',
       'saves_90', 'YC','saves','bonus', 'bps',
       'starts','XGC', 'XGC_90',
       'GC_90'],
    'DEF': ['cost', 'pts_game', 'selected%',
       'total_pts', 'value_season', 'minutes', 'G',
       'A', 'clean_sheets', 'GC', 'own_G','YC', 'RD', 'bonus', 'bps',
       'I', 'C', 'T', 'ict_i', 'starts',
       'XG', 'XA', 'XGI',
       'XG_90', 'XA_90',
       'XGI_90'],
    'MID':['cost', 'pts_game', 'selected%', 
      'total_pts', 'val_ssn', 'minutes',
       'G', 'A','pnlty_missed', 'YC',
       'RC', 'bonus', 'bps', 'I', 'C',
       'T', 'I_idx', 'starts', 'XG', 'XA',
       'XGI', 'XG90',
       'XA90', 'XGI90'],
       'FWD':['cost', 'pts_game', 'selected%', 
      'total_pts', 'val_ssn', 'minutes',
       'G', 'A','pnlty_missed', 'YC',
       'RC', 'bonus', 'bps', 'I', 'C',
       'T', 'I_idx', 'starts', 'XG', 'XA',
       'XGI', 'XG90',
       'XA90', 'XGI90']

}

def pizzaplot(params,values,min_range,max_range,name,team):
    
    baker = PyPizza(
    params=params,
    min_range=min_range,        # min range values
    max_range=max_range,        # max range values
    background_color="#222222", straight_line_color="#000000",
    last_circle_color="#000000", last_circle_lw=2.5, straight_line_lw=1,
    other_circle_lw=0, other_circle_color="#000000", inner_circle_size=20,
    )
    fig, ax = baker.make_pizza(
        values,                     # list of values
        figsize=(8, 8),             # adjust figsize according to your need
        color_blank_space="same",   # use same color to fill blank space
        blank_alpha=0.4,            # alpha for blank-space colors
        param_location=110,         # where the parameters will be added
        kwargs_slices=dict(
            facecolor="#1A78CF", edgecolor="#000000",
            zorder=1, linewidth=1,
        ),                          # values to be used when plotting slices
        kwargs_params=dict(
            color="#F2F2F2", fontsize=12, zorder=5,
            fontproperties=font_normal.prop, va="center"
        ),                          # values to be used when adding parameter
        kwargs_values=dict(
            color="#000000", fontsize=12,
            fontproperties=font_normal.prop, zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="#1A78CF",
                boxstyle="round,pad=0.2", lw=1
            )
        )                           # values to be used when adding parameter-values
    )
    # add title
    fig.text(
        0.515, 0.97, f"{name} - {team}", size=18,
        ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
    )

    # add subtitle
    fig.text(
        0.515, 0.942,
        "Season 2023-24",
        size=15,
        ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
    )

    # add credits
    CREDIT_1 = "data: statsbomb"
    CREDIT_2 = "created by: youssef alarby"

    fig.text(
        0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
        fontproperties=font_italic.prop, color="#F2F2F2",
        ha="right"
    )
   
    
    return fig

def find_low_high(data,param):
    low=[]
    high=[]
    for col in param:
        low.append(data[col].min()-1)
        high.append(data[col].max()+1)
    return low,high

def prepare_data(data,param,name):
    val=[]
    player=data[data['web_name']==name]
    for col in param:
        val.append(player.iloc[0][col])
    return val

st.title('EPL 2023/2024 stats')
st.subheader('choose the player that you want to see his stats')
order=['GK','DEF','MID','FWD']
pos=st.selectbox('select a position',
                 pd.Categorical(df['element_type'],categories=order,ordered=True).sort_values().unique(),index=None)
teams=df['team'].sort_values().unique().tolist()
team=st.selectbox('select a team',teams,index=None)

names=df[(df['element_type']==pos) & (df['team']== team)]['web_name'].to_list()
if pos and team:
    name=st.selectbox('select name',names,index=None)
    if name:
        param=pos_col[pos]
        param2=pos_name[pos]
        values=prepare_data(df,param,name)
        min_range,high_range=find_low_high(df,param)
        plot=pizzaplot(param2,values,min_range,high_range,name,team)
        st.pyplot(plot)
