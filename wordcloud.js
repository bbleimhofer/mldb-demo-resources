// drawn from http://www.jasondavies.com/word-cloud/
function drawCloud(input_words) {
  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", layout.size()[0]).attr("height", layout.size()[1])
      .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
      .selectAll("text").data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) { return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"; })
        .text(function(d) { return d.text; });
  }
  var fill = d3.scale.category20();
  var layout = d3.layout.cloud()
      .size(800, 300]).words(input_words).padding(8).rotate(0)
      .fontSize(function(d) { return 2*d.size+10; })
      .on("end", draw);
  layout.start();
}
