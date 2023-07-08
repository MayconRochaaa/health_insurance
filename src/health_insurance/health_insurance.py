import os
import numpy        as np
import pandas       as pd
import pickle
import inflection

class HealthInsurance( object ):
    
    def __init__( self ):
        
        self.home_path =                        os.path.dirname(os.path.abspath(''))
        
        self.model_path =                       os.path.join(self.home_path,'models')
        self.features_path =                    os.path.join(self.model_path,'features')
        
        self.age_scaler =                       pickle.load( open( os.path.join(self.features_path,'age_scaler.pkl'),                       'rb' ) )
        self.annual_premium_scaler =            pickle.load( open( os.path.join(self.features_path,'annual_premium_scaler.pkl'),            'rb' ) ) 
        self.fe_policy_sales_channel_scaler =   pickle.load( open( os.path.join(self.features_path,'fe_policy_sales_channel_scaler.pkl'),   'rb' ) ) 
        self.target_encode_gender_scaler =      pickle.load( open( os.path.join(self.features_path,'target_encode_gender_scaler.pkl'),      'rb' ) )
        self.target_encode_region_code_scaler = pickle.load( open( os.path.join(self.features_path,'target_encode_region_code_scaler.pkl'), 'rb' ) )
        self.total_expense_scaler =             pickle.load( open( os.path.join(self.features_path,'total_expense_scaler.pkl'),             'rb' ) )
        self.vintage_scaler =                   pickle.load( open( os.path.join(self.features_path,'vintage_scaler.pkl'),                   'rb' ) )
        
    def data_cleaning( self, df1 ):
        # 1.1. Rename Columns
        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, df1.columns.tolist()))
        df1.columns = cols_new
        
        df1['vehicle_damage'] = [1 if i=='Yes' else 0 for i in df1['vehicle_damage']]
        df1['vehicle_age'] = ['below_1_year' if i=='< 1 Year' else 'between_1_2_year' if i=='1-2 Year' else 'over_2_year' for i in df1['vehicle_age']]
        
        original_cols = df1.columns.to_list()
        
        return df1

    
    def feature_engineering( self, df2 ):
        # 2.0. Feature Engineering

        df2['total_expense'] = (df2['annual_premium']/12)*((np.floor(df2['vintage']/30))+1)

        df2['quadrimestre'] = np.floor(df2['vintage']/30)+1
        df2['quadrimestre'] = df2['quadrimestre'].apply(lambda x: 1 if x<4 else 2 if (x>=4 and x<8) else 3)
        
        return df2
    
    
    def data_preparation( self, df5 ):
        
        # Age - MinMaxScaler
        df5['age'] = self.age_scaler.transform( df5[['age']].values )
        
        # anual premium - StandarScaler
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values )

        # policy_sales_channel - Target Encoding / Frequency Encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.fe_policy_sales_channel_scaler )

        # gender - One Hot Encoding / Target Encoding
        df5.loc[:, 'gender'] = df5['gender'].map( self.target_encode_gender_scaler )

        # region_code - Target Encoding / Frequency Encoding
        df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encode_region_code_scaler )

        # vehicle_age - One Hot Encoding / Frequency Encoding
        df5 = pd.get_dummies( df5, prefix='vehicle_age', columns=['vehicle_age'] )
        
        df5['total_expense'] = self.total_expense_scaler.transform( df5[['total_expense']].values )
        
        # Vintage - MinMaxScaler
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )

        
        # Feature Selection
        cols_selected = ['annual_premium', 'vintage', 'total_expense', 'age', 'region_code', 'vehicle_damage', 'previously_insured',
                 'policy_sales_channel', 'vehicle_age_between_1_2_year', 'vehicle_age_below_1_year']
        
        return df5[ cols_selected ]
    
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into original data
        original_data['score'] = pred[:, 1].tolist()
        original_data = original_data.sort_values(by='score', ascending=False)
        
        return original_data.to_json( orient='records', date_format='iso' )
