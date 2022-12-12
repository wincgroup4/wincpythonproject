# PLOTLY - plot graph for Digital-Cash Ratio Statistics
# '''
# @author: WinC Python project Group4
# """

from plotly import graph_objs as go
from plotly.subplots import make_subplots


def draw_chart(ratio_df, html_file):
    fig = make_subplots(rows=2, cols=2)
    x = ratio_df['bank']
    y = ratio_df['CASH']
    y1 = ratio_df['DIGITAL']
    y2 = ratio_df['INVALID']
    s = ratio_df['ratio']
    max_value = ratio_df['ratio'].max()
    # max_ratios = opp[opp['ratio'] == max_value]['bank'].values
    max_ratios = ratio_df[ratio_df['ratio'] == max_value]['bank'].index.to_list()

    # Digital-Cash-Invalid Table view
    fig.add_trace(
            go.Table(
                columnwidth=[8,2,2,2,2],
                header=dict(values=ratio_df.columns),
                cells=dict(values=[ratio_df[k].tolist() for k in ratio_df.columns[:]],
                align = "center"
            )))
    # Chart views
    fig.add_bar(x=x,
                y=y,
                name='cash',
                row=2,col=1)
    fig.add_bar(x=x,
                y=y1,
                name='digital',
                row=2,col=1)
    fig.add_bar(x=x,
                y=y2,
                name='invalid',
                row=2,col=1)
    fig.add_scatter(x=x,
                y=s,
                mode="markers",
                marker=dict(size=10, color="LightSeaGreen"),
                name="ratio Digital/Cash",
                row=2,col=2,
                text='ratio'
                    )
    for val in max_ratios:
        fig.add_annotation(x=val,
                        y=max_value,
                        text=(str(max_value)),
                        row=2,col=2,
                    
                    )
    
    fig.update_xaxes(title_text="Digital-Cash-Invalid transaction",row=2, col=1)
    fig.update_xaxes(title_text="Digital-to-Cash ratio",row=2, col=2)
    fig.update_yaxes(title_text="Number of transactions", range=[0, 50000], row=2, col=1, dtick=5000)
    fig.update_layout(height=900, width=800, title_text="<b>Digital/Cash Transactions</b> statistics")
    fig.write_html(html_file)