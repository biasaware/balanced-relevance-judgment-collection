# Balancing Large-scale Relevance Judgement Collections for Fair Neural Ranking
This repository contains the code and resources for our proposed approach to create a balanced relevance-judgment collection that diminished the bias conveyed to neural rankers. The main focus of this approach would be automatically building query-document pairs that can be used for training neural rankers. We then show how combining our proposed query-document pairs with existing gold standard relevance judgement datasets can lead to the training of less biased neural rankers that have competitive retrieval effectiveness. We conduct our experiments on the MSMARCO passage collection and use three widely adopted psychological and stereotypical gender bias measurement methods to show that decrease in bias happens effectively regardless of how gender biases are measured.


#### Table 1: Model effectiveness on augmented datasets. * indicates statistically significant decrease in effectiveness.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Training Dataset</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Ratio</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">MRR@10</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">% Reduction</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Original Set</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3110</span></td>
    <td class="tg-lqy6"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="4"><br><br><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Augmented Datasets</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.05</span></td>
    <td class="tg-ktyi"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3133</span></td>
    <td class="tg-eelb"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.74%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.15</span></td>
    <td class="tg-ktyi"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3078</span></td>
    <td class="tg-eelb"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-1.03%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.25</span></td>
    <td class="tg-ktyi"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3036</span></td>
    <td class="tg-eelb"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-2.38%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.35</span></td>
    <td class="tg-ktyi"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.2949</span></td>
    <td class="tg-eelb"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-5.18%*</span></td>
  </tr>
</tbody>
</table>



#### Table 2: Impact of training on augmented dataset on the difference in psychological characteristics of gender-affiliated queries.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Neural Re-ranker Model</th>
    <th class="tg-0pky" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Training Dataset</span></th>
    <th class="tg-fymr"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Affective Processes</span></th>
    <th class="tg-fymr"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Cognitive Processes</span></th>
    <th class="tg-fymr"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Drives</span></th>
    <th class="tg-fymr"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Personal Concerns</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="7">BERT-base-uncased</td>
    <td class="tg-c3ow" rowspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Original Dataset </span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span> <a href="https://github.com/aminbigdeli/bias-aware-PRF/tree/main/results/runs/PRF" target="_top"> (Run)</td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0315</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0725</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0545</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0600</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0290</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0521</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0641</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0829</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Difference</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0025</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0204</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0095</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0229</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Augmented Dataset</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0304</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0730</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0536</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0546</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0288</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0563</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0624</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0747</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Difference</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0016</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0167</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0088</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0201</span></td>
  </tr>
  <tr>
    <td class="tg-c3ow" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">%Reduction</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">34.33%</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">18.03%</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">7.34%</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">12.19%</span></td>
  </tr>
</tbody>
</table>



#### Table 3: The impact of training BERT-base-uncased on the augmented dataset on proxy measures of bias based on different neutral query sets.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2">Neural Re-ranker Model</th>
    <th class="tg-0lax" rowspan="2">Query Set</th>
    <th class="tg-0lax" rowspan="2">Training Set</th>
    <th class="tg-0lax" colspan="4">ARaB</th>
    <th class="tg-0lax" colspan="2">LIWC</th>
  </tr>
  <tr>
    <td class="tg-0lax">TF</td>
    <td class="tg-0lax">TF (%)</td>
    <td class="tg-0lax">Boolean</td>
    <td class="tg-0lax">Boolean (%)</td>
    <td class="tg-0lax">Male Female Diff</td>
    <td class="tg-0lax"> Improvement (%)</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="4">BERT-base-uncased</td>
    <td class="tg-0lax" rowspan="2">1765 Neutral Queries</td>
    <td class="tg-0lax">Original Dataset</td>
    <td class="tg-baqh">0.072</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.059</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.0117</td>
    <td class="tg-baqh">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">Augmented Dataset</td>
    <td class="tg-baqh">0.059</td>
    <td class="tg-baqh">18.05%</td>
    <td class="tg-baqh">0.049</td>
    <td class="tg-baqh">16.49%</td>
    <td class="tg-baqh">0.0110</td>
    <td class="tg-baqh">5.98%</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2">215 Social Problematic Queries</td>
    <td class="tg-0lax">Original Dataset </td>
    <td class="tg-baqh">0.029</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.017</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.0060</td>
    <td class="tg-baqh">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">Augmented Dataset</td>
    <td class="tg-baqh">0.019</td>
    <td class="tg-baqh">34.48%</td>
    <td class="tg-baqh">0.011</td>
    <td class="tg-baqh">35.29%</td>
    <td class="tg-baqh">0.0057</td>
    <td class="tg-baqh">5.00%</td>
  </tr>
</tbody>
</table>


#### Table 4: Comparative Analysis between BERT-Tiny trained on the augmented dataset and ADVBERT Model
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2">Neural Re-ranker Model</th>
    <th class="tg-0pky" rowspan="2">Query Set</th>
    <th class="tg-0pky" rowspan="2">Training Set</th>
    <th class="tg-0pky" rowspan="2">MRR<br>@10<br></th>
    <th class="tg-0pky" colspan="4">ARaB</th>
    <th class="tg-0pky" colspan="2">LIWC</th>
  </tr>
  <tr>
    <td class="tg-0pky">TF</td>
    <td class="tg-0pky">TF (%)</td>
    <td class="tg-0pky">Boolean</td>
    <td class="tg-0pky">Boolean (%)</td>
    <td class="tg-0pky">Male Female Diff</td>
    <td class="tg-0pky"> Improvement (%)</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" rowspan="6">BERT-Tiny</td>
    <td class="tg-0pky" rowspan="3">1765 Neutral Queries</td>
    <td class="tg-0pky">Original Dataset</td>
    <td class="tg-c3ow">0.219</td>
    <td class="tg-c3ow">0.076</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0630</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0121</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">Augmented Dataset</td>
    <td class="tg-c3ow">0.199</td>
    <td class="tg-c3ow">0.047</td>
    <td class="tg-c3ow">38.15%</td>
    <td class="tg-c3ow">0.0428</td>
    <td class="tg-c3ow">32.08%</td>
    <td class="tg-c3ow">0.0108</td>
    <td class="tg-c3ow">10.74%</td>
  </tr>
  <tr>
    <td class="tg-0lax">ADVBERT</td>
    <td class="tg-baqh">0.189</td>
    <td class="tg-baqh">0.064</td>
    <td class="tg-baqh">15.78%</td>
    <td class="tg-baqh">0.05884</td>
    <td class="tg-baqh">7.41%</td>
    <td class="tg-baqh">0.0091</td>
    <td class="tg-baqh">25.08%</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">215 Social Problematic Queries</td>
    <td class="tg-0pky">Original Dataset </td>
    <td class="tg-c3ow">0.162</td>
    <td class="tg-c3ow">0.005</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0067</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0054</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">Augmented Dataset</td>
    <td class="tg-c3ow">0.163</td>
    <td class="tg-c3ow">0.001</td>
    <td class="tg-c3ow">79.19%</td>
    <td class="tg-c3ow">0.0002</td>
    <td class="tg-c3ow">96.81%</td>
    <td class="tg-c3ow">0.0048</td>
    <td class="tg-c3ow">11.11%</td>
  </tr>
  <tr>
    <td class="tg-0lax">ADVBERT</td>
    <td class="tg-baqh">0.149</td>
    <td class="tg-baqh">0.009</td>
    <td class="tg-baqh">-85.90%</td>
    <td class="tg-baqh">0.0076</td>
    <td class="tg-baqh">-13.88%</td>
    <td class="tg-baqh">0.0046</td>
    <td class="tg-baqh">14.81%</td>
  </tr>
</tbody>
</table>

