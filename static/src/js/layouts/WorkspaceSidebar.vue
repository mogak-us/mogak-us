<script setup>
defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
});
</script>
<template>
  <div class="w-60 bg-amber-300 border-r-amber-800 border-r-2 h-screen">
    <div class="p-4">
      <h3>{{ workspace.name }}</h3>
      <p>ID: {{ workspace.id }}</p>
    </div>
  </div>
</template>
