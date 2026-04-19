<template>
  <div>
    <div ref="SocialMediaGraph"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "SocialMediaGraph",
  computed: {
    ...mapGetters("datapage", ["socialMediaData"]),
  },
  mounted() {
    this.buildSocialMediaGraph();
  },
  methods: {
  }
}

</script>

<style scope>

</style>