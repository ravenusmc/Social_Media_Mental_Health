<template>
  <div>
    <Top></Top>
    <AgeScreenTime/>
  </div>
</template>

<script>
// @ is an alias to /src
import Top from '@/components/data/Top.vue'
import AgeScreenTime from '@/components/graphs/AgeScreenTime.vue'

export default {
  name: 'DataView',
  components: {
    Top, 
    AgeScreenTime, 
  }
}

</script>
