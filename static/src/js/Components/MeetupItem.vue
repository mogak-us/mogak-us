<script setup>
defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
  meetup: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj && "date" in obj
  },
});
</script>

<template>
  <div class="meetup-item p-4 bg-gray-100 shadow rounded-lg mb-4">
    <h3 class="text-lg font-semibold mb-1">{{ meetup.name }}</h3>
    <p class="text-sm text-gray-600 mb-2">Date: {{ meetup.date }}</p>
    <a :href='`/workspaces/${workspace.id}/meetups/${meetup.id}`' class="text-blue-500 hover:underline">View Details</a>
  </div>
</template>

<style scoped>
.meetup-item {
  border: 1px solid #e2e8f0;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 8px;
  background-color: #f7fafc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
