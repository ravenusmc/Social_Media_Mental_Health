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
      
    }
  }
}

</script>