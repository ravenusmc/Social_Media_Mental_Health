<template>
  <div>
    <div ref="ExerciseVsHappinessGraph"></div>
  </div>
</template>


<script>
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ExerciseVsSleep",
  computed: {
    ...mapGetters("datapage", ["ExerciseVsHappiness"]),
  },
  mounted() {
    this.buildExerciseVsHappinessGraph();
  },
  methods: {
    buildExerciseVsHappinessGraph() {

      // Remove old SVG
      d3.select(this.$refs.ExerciseVsHappinessGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.ExerciseVsHappinessGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
      
      // X axis ()
      const x = d3.scaleLinear()
        .domain([
          d3.min(this.ExerciseVsHappiness, d => d[0]),
          d3.max(this.ExerciseVsHappiness, d => d[0])
        ])
        .range([0, width]);
      
      svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));
      
      // Y axis (Stress)
      const y = d3.scaleLinear()
        .domain([
          0,
          d3.max(this.ExerciseVsHappiness, d => d[1])
        ])
        .range([height, 0]);

      svg.append("g")
        .call(d3.axisLeft(y));
      
      // Add dots
      svg.append("g")
        .selectAll("circle")
        .data(this.ExerciseVsHappiness)
        .enter()
        .append("circle")
        .attr("cx", d => x(d[0]))
        .attr("cy", d => y(d[1]))
        .attr("r", 4);

    }
  }

}

</script>