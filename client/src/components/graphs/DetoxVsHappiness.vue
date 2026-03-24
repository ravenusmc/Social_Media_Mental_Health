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

      
    }
  }
}

</script>