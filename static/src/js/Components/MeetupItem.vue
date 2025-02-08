<script setup>
defineProps({
  meetup: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj && "date" in obj
  },
});
</script>

<template>
  <div class="meetup-item">
    <a :href='`/meetups/${meetup.id}`'>View</a>
    <h3>{{ meetup.name }}</h3>
    <p>Date: {{ meetup.date }}</p>
  </div>
</template>

<style scoped>
.meetup-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
