<template>
  <div>
    <div ref="DetoxVsHappinessGraph"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "DetoxVsHappiness",
  computed: {
    ...mapGetters("datapage", ["detoxDaysVsHappiness"]),
  },
  mounted() {
    this.buildDetoxVsHappinessGraph();
  },
  methods: {
    buildDetoxVsHappinessGraph() {

      // Remove old SVG
      d3.select(this.$refs.DetoxVsHappinessGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.DetoxVsHappinessGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      
      // X axis (Detox)
      const x = d3.scaleLinear()
        .domain([
          d3.min(this.detoxDaysVsHappiness, d => d[0]),
          d3.max(this.detoxDaysVsHappiness, d => d[0])
        ])
        .range([0, width]);
      
      svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));
      
      // Y axis (Stress)
      const y = d3.scaleLinear()
        .domain([
          0,
          d3.max(this.detoxDaysVsHappiness, d => d[1])
        ])
        .range([height, 0]);
      svg.append("g")
        .call(d3.axisLeft(y));
      
      // Add dots
      svg.append("g")
        .selectAll("circle")
        .data(this.detoxDaysVsHappiness)
        .enter()
        .append("circle")
        .attr("cx", d => x(d[0]))
        .attr("cy", d => y(d[1]))
        .attr("r", 4);
      
      svg
        .append("text")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Detox (10 - Great)");
      
      // Y-Axis Label 
      svg
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Happeniness (1-10)");

      
    }
  }
}

</script>