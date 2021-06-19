# Balancing Large-scale Relevance Judgement Collections for Fair Neural Ranking
This repository contains the code and resources for our proposed approach to create a balanced relevance-judgment collection that diminishes the bias conveyed to neural rankers. The main focus of this approach is to propose an automated method to generate pairs of query and relevant documents that have controlled degrees of bias. Figure below shows our proposed methodology.

<p align="center">
  <img src="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/methodology.png">
</p>

As you can see, Table 1 shows some examples of balanced query-document pairs. In this table each female and male document-pairs share similar level of psychological characteristics in their passages.
#### Table 1: Examples of paired gendered queries in our generated dataset
<table class="tg">
<thead>
  <tr>
    <th class="tg-1wig">Examples</th>
    <th class="tg-1wig"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Gender Affiliation</span></th>
    <th class="tg-1wig"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Generated Query</span></th>
    <th class="tg-1wig"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Source Passage</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Sample Pair 1</span></td>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">when did winnie davis pass away</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">WINNIE DAVIS passed away. The obituary was featured in The Impartial Reporter on June 6, 2013.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">when did maya angelou die</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">13 of Maya Angelou's best quotes. Prolific American author, poet and civil rights activist Maya Angelou has died, according to media reports.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Sample Pair 2</span></td>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">vess carlos worth</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">$15 Million. Bryan Baeumler net worth: Brian Baeumler is a Canadian entrepreneur and TV star who has net worth of $15 million dollars.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">lesley stahl net worth</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Lesley Stahl net worth: Lesley Stahl is an American television journalist who has a net worth of $20 million dollars.Lesley Stahl was born in Lynn, Massachusetts, and went on to graduate from Wheaton College.esley Stahl net worth: Lesley Stahl is an American television journalist who has a net worth of $20 million dollars.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Sample Pair 3</span></td>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">where is ronald brown from</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Ronald Brown 13,811 people named Ronald Brown found in California, Florida and 50 other states. Click a state below to find Ronald more easily.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">where is elizabeth blackwell from</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Elizabeth Blackwell 774 people named Elizabeth Blackwell found in North Carolina, Texas and 47 other states. Click a state below to find Elizabeth more easily.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Sample Pair 4</span></td>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">who is samuel khouth</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Samuel Vincent Khouth (born October 5, 1971) is a Canadian voice actor and singer.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">who was barbara stanwyck</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Barbara Stanwyck. Barbara Stanwyck (born Ruby Catherine Stevens; July 16, 1907 </span><span style="color:#000;background-color:transparent">January 20, 1990) was an American actress, model and dancer.</span></td>
  </tr>
</tbody>
</table>

## Utility
We now show how combining our proposed query-document pairs with existing gold standard relevance judgement datasets can lead to the training of less biased neural rankers that have competitive retrieval effectiveness. For this purpose, we augment the small training set of MS MARCO with data from our generated query-document pairs using different ratios with 10\% increments. For instance, a 15% ratio would mean that we augment the MS MARCO training set with an additional n query-document pairs from our dataset where n is equivalent to 15\% of the size of the MS MARCO small training set. Based on the augmented datasets, we leverage the BERT-base-uncased transformer model for passage ranking  and train it on the original dataset, i.e., the small training set of MS MARCO, as well as the newly developed augmented datasets and compare their effectiveness in Table 2.

#### Table 2: Model effectiveness on augmented datasets. * indicates statistically significant decrease in effectiveness.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Neural Re-ranker Model</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Training Dataset</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Ratio</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">MRR@10</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">% Reduction</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="5">BERT-base-uncased</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Original Set</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3110</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="4"><br><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Augmented Datasets</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.05</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3133</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.74%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.15</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3078</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-1.03%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.25</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.3036</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-2.38%</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.35</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.2949</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-5.18%*</span></td>
  </tr>
</tbody>
</table>

## Bias Measurement
In order measure bias we use three widely adopted psychological and stereotypical gender bias measurement methods to show that decrease in bias happens effectively regardless of how gender biases are measured. We adopt two strategies to measure gender biases. The first approach relies on measuring differences observed across pairs of gender-affiliated queries. As you can see in Table 3, when the model is trained on the augmented dataset, the difference between psychological charactiristics of documents associated with male and female queries has decreased significantly.

#### Table 3: Impact of training on augmented dataset on the difference in psychological characteristics of gender-affiliated queries.
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
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span> <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/female_affiliated_queries/bert_base_uncased_original_dataset.trec" target="_top"> (Run)</td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0315</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0725</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0545</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0600</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span> <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/male_affiliated_queries/bert_base_uncased_original_dataset.trec" target="_top"> (Run)</td>
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
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Female </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span> <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/female_affiliated_queries/bert_base_uncased_augmented_dataset_0.25.trec" target="_top"> (Run)</td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0304</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0730</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0536</span></td>
    <td class="tg-dvpl"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">0.0546</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Male </span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Queries</span> <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/male_affiliated_queries/bert_base_uncased_augmented_dataset_0.25.trec" target="_top"> (Run)</td>
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



#### Table 4: The impact of training BERT-base-uncased on the augmented dataset on proxy measures of bias based on different neutral query sets.
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
    <td class="tg-0lax">Original Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/1765_neutral_queries/bert_base_uncased_original_dataset.trec" target="_top"> (Run)</td>
    <td class="tg-baqh">0.072</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.059</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.0117</td>
    <td class="tg-baqh">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">Augmented Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/1765_neutral_queries/bert_base_uncased_augmented_dataset_25.trec" target="_top"> (Run)</td>
    <td class="tg-baqh">0.059</td>
    <td class="tg-baqh">18.05%</td>
    <td class="tg-baqh">0.049</td>
    <td class="tg-baqh">16.49%</td>
    <td class="tg-baqh">0.0110</td>
    <td class="tg-baqh">5.98%</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2">215 Social Problematic Queries</td>
    <td class="tg-0lax">Original Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/215_neutral_queries/bert_base_uncased_original_dataset.trec" target="_top"> (Run)</td>
    <td class="tg-baqh">0.029</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.017</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">0.0060</td>
    <td class="tg-baqh">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">Augmented Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/215_neutral_queries/bert_base_uncased_augmented_dataset_0.25.trec" target="_top"> (Run)</td>
    <td class="tg-baqh">0.019</td>
    <td class="tg-baqh">34.48%</td>
    <td class="tg-baqh">0.011</td>
    <td class="tg-baqh">35.29%</td>
    <td class="tg-baqh">0.0057</td>
    <td class="tg-baqh">5.00%</td>
  </tr>
</tbody>
</table>


#### Table 5: Comparative Analysis between BERT-Tiny trained on the augmented dataset and ADVBERT Model
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
    <td class="tg-0pky">Original Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/1765_neutral_queries/bert_tiny_original_dataset.trec" target="_top"> (Run)</td>
    <td class="tg-c3ow">0.219</td>
    <td class="tg-c3ow">0.076</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0630</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0121</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">Augmented Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/1765_neutral_queries/bert_tiny_augmented_dataset_25.trec"> (Run)</td>
    <td class="tg-c3ow">0.199</td>
    <td class="tg-c3ow">0.047</td>
    <td class="tg-c3ow">38.15%</td>
    <td class="tg-c3ow">0.0428</td>
    <td class="tg-c3ow">32.08%</td>
    <td class="tg-c3ow">0.0108</td>
    <td class="tg-c3ow">10.74%</td>
  </tr>
  <tr>
    <td class="tg-0lax">ADVBERT <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/1765_neutral_queries/ADVBERT_tiny.trec"> (Run)</td>
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
    <td class="tg-0pky">Original Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/215_neutral_queries/bert_tiny_original_dataset.trec"> (Run)</td>
    <td class="tg-c3ow">0.162</td>
    <td class="tg-c3ow">0.005</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0067</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">0.0054</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">Augmented Dataset <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/215_neutral_queries/bert_tiny_augmented_dataset_0.25.trec"> (Run)</td>
    <td class="tg-c3ow">0.163</td>
    <td class="tg-c3ow">0.001</td>
    <td class="tg-c3ow">79.19%</td>
    <td class="tg-c3ow">0.0002</td>
    <td class="tg-c3ow">96.81%</td>
    <td class="tg-c3ow">0.0048</td>
    <td class="tg-c3ow">11.11%</td>
  </tr>
  <tr>
    <td class="tg-0lax">ADVBERT <a href="https://github.com/biasaware/balanced-relevance-judgment-collection/blob/main/results/trec_runs/215_neutral_queries/ADVBERT_tiny.trec"> (Run)</td>
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

