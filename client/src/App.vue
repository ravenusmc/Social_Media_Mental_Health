<template>
  <div>
    <NavBar />
    <router-view/>
    <!-- <FootComponent /> -->
  </div>
</template>

<script>
import NavBar from "./components/common/NavBar.vue";
// import FootComponent from "@/components/common/FootComponent.vue";

export default {
  name: 'App',
  components: {
    NavBar,
    // FootComponent,
  }
}
</script>

<style>

</style>
