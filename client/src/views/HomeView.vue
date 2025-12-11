<template>
  <div>
    <TitleArea></TitleArea>
    <Purpose/>
  </div>
</template>

<script>
// @ is an alias to /src
import TitleArea from '@/components/home/TitleArea.vue'
import Purpose from '@/components/home/Purpose.vue'

export default {
  name: 'HomeView',
  components: {
    TitleArea, 
    Purpose, 
  }
}
</script>
