<script setup>
import WorkspaceSidebar from '@/layouts/WorkspaceSidebar.vue'

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
})

</script>

<template>
  <div class="w-full flex bg-white text-black">
    <WorkspaceSidebar :workspace="workspace" />
    <div class="w-full mx-8 mt-12">
      <slot />
    </div>
  </div>
</template>
