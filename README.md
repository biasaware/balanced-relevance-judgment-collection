# Balancing Large-scale Relevance Judgement Collections for Fair Neural Ranking
This repository contains the code and resources for our proposed approach to create a balanced relevance-judgment collection that diminished the bias conveyed to neural rankers. The main focus of this approach would be automatically building query-document pairs that can be used for training neural rankers. We then show how combining our proposed query-document pairs with existing gold standard relevance judgement datasets can lead to the training of less biased neural rankers that have competitive retrieval effectiveness. We conduct our experiments on the MSMARCO passage collection and use three widely adopted psychological and stereotypical gender bias measurement methods to show that decrease in bias happens effectively regardless of how gender biases are measured.



<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
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
    <td class="tg-0lax">(%)</td>
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



