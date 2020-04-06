from django import forms


class WeightLossAnalysisForm(forms.Form):
    gender = forms.ChoiceField(label='Gender',
                               choices=[('woman', 'Woman'),
                                        ('Man', 'Man')])
    current_weight = forms.ChoiceField(label='Current Weight span',
                                       choices=[('< 60 kg', '< 60 kg'),
                                                ('60-70 kg', '60-70 kg'),
                                                ('70-80 kg', '70-80 kg'),
                                                ('80-90 kg', '80-90 kg'),
                                                ('90-100 kg', '90-100 kg'),
                                                ('+100 kg', '+100 kg')])
    expected_weight_loss = forms.ChoiceField(label='How much do you want to lose?',
                                             choices=[('1-3 kg', '1-3 kg'),
                                                      ('3-6 kg', '3-6 kg'),
                                                      ('6-9 kg', '6-9 kg'),
                                                      ('9-12 kg', '9-12 kg'),
                                                      ('12-15 kg', '12-15 kg'),
                                                      ('+15 kg', '+15 kg')])
    current_age = forms.ChoiceField(label='Current age span?',
                                    choices=[('< 20', '< 20'),
                                             ('20-30', '20-30'),
                                             ('30-40', '30-40'),
                                             ('40-50', '40-50'),
                                             ('50-60', '50-60'),
                                             ('60 +', '60 +')])
    training_level = forms.ChoiceField(label='What level of training do you prefer?',
                                       choices=[('starting out', 'Starting Out'),
                                                ('firm tummy and thighs',
                                                 'Firm Tummy and Thighs'),
                                                ('Not so much time and quick results',
                                                 'Not so much time and quick results'),
                                                ('Want a challenge',
                                                 'Want a challenge'),
                                                ('Pregnant or had a baby within 3 years', 'Pregnant or had a baby within 3 years')])
