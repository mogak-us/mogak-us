<template>
  <div class="workspace-item">
    <a :href='`/workspaces/${workspace.id}`'>View</a>
    <h3>{{ workspace.name }}</h3>
    <p>ID: {{ workspace.id }}</p>
  </div>
</template>

<script setup>
defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
});
</script>

<style scoped>
.workspace-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
