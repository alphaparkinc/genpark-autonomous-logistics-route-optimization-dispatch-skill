from client import AutonomousLogisticsRouteOptimizationDispatchClient

def main():
    client = AutonomousLogisticsRouteOptimizationDispatchClient()
    res = client.optimize_delivery_fleet([{'id': 'ord_01'}], [{'id': 'truck_01'}])
    print('Orders Dispatched: ' + str(res['total_orders_dispatched']) + ' | Fuel Savings: $' + str(res['fuel_cost_savings_usd']))
    print('Fleet Utilization: ' + str(res['fleet_utilization_pct']) + '%')
    for r in res['active_routes']:
        print('  [' + r['vehicle_id'] + '] ' + str(r['stops_count']) + ' stops (' + str(r['total_distance_km']) + 'km, SLA: ' + str(r['on_time_sla_pct']) + '%)')

if __name__ == '__main__':
    main()
