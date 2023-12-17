import dash
from dash import dcc, html

import pandas as pd
from dash.dependencies import Input, Output, State
import model




#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__, 
    #external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
    )
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(
    [
        html.Div(
            [html.Img(src=app.get_asset_url("dash-logo.png"))], className="app__banner"
    ),

    html.Div(
        [
        html.Div(
            [
                html.Div(
                    [
                        html.H1(
                            "Advanced Sentiment Analysis for Sephora Website Product Reviews",
                            className="uppercase title",
                        ),
                        html.Span(
                            "This advanced  text classification model accurately categorizes your input into the following tags:", style={'padding': '20px'}
                        ),
                        html.Br(),                        
                        html.Span(
                            "Tag confidence simply shows how sure the model is about each tag", style={'padding': '10px'}
                        ),
                        html.Br(),                        
                        html.Span(
                            "Sentiment confidence reflects the model's certainty about the sentiment: Positive/Neutral/Negative", style={'padding': '10px'}
                        ),  
                        html.Br(),
                        html.Br(),                        
                        html.Span("Very Negative", style={'color': '#9c1313', 'border-radius': '5px', 'border-width': '2px', 'border-style': 'solid', 'border-color': '#b8c2d4', 'padding': '2px','margin-right': '5px'} ),
                        html.Span("Negative",      style={'color': '#dc1b1b', 'border-radius': '5px', 'border-width': '2px', 'border-style': 'solid', 'border-color': '#b8c2d4', 'padding': '2px', 'margin-right': '5px'} ),
                        html.Span("Neutral",       style={'color': '#837738', 'border-radius': '5px', 'border-width': '2px', 'border-style': 'solid', 'border-color': '#b8c2d4', 'padding': '2px', 'margin-right': '5px'} ),
                        html.Span("Positive",      style={'color': '#94b552', 'border-radius': '5px', 'border-width': '2px', 'border-style': 'solid', 'border-color': '#b8c2d4', 'padding': '2px', 'margin-right': '5px'} ),
                        html.Span("Very Positive", style={'color': '#458338', 'border-radius': '5px', 'border-width': '2px', 'border-style': 'solid', 'border-color': '#b8c2d4', 'padding': '2px'} ),                                                                               
                    ], style = {'background':'#ffffff'}
                ),
            ],
        className="app__header",
    ),
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H3('Share your thoughts and reviews so we can analyze them:'),
                            dcc.Textarea(
                                id="input-id",
                                value ="Wow, what a fabulous story!",
                                style={'height': '300px', 'width': '100%'}
                            )
                        ], className ='six columns'
                    ),
                    
                    html.Div(
                        [
                            html.H3('Tag'),
                            html.Div(
                                id='my-sent', 
                                className="row"
                                ),
                            html.Div(
                                id='my-conf', 
                                className="row"
                                ),
                            html.Div(
                                id='my-tag', 
                                className="row"
                                ),
                        ], className='six columns'
                    ),                    
                ],
            )
        ], className="container card app__content bg-white",
    )
    ], className="app__container",
)
],style = {'background':'#f5f7fa'}
)


@app.callback(
    [Output(component_id='my-sent', component_property='children'),
    Output(component_id='my-conf', component_property='children'),
    Output(component_id='my-tag', component_property='children')
    ],
    [Input(component_id='input-id', component_property='value')]
)
def update_output_div(input_value):
    tag, tag_prob, sent_prob = model.predict_response([input_value])
    return f"Tag: {tag}", f"Tag confidence: {tag_prob*100:.1f}%", f"Sentiment Confidence: {sent_prob*100:.1f}%"



if __name__ == "__main__":
    app.run_server(debug=True)